# -*- coding: utf-8 -*-

##############################################################################
#                        2011 E2OpenPlugins                                  #
#                                                                            #
#  This file is open source software; you can redistribute it and/or modify  #
#     it under the terms of the GNU General Public License version 2 as      #
#               published by the Free Software Foundation.                   #
#                                                                            #
##############################################################################

from enigma import eConsoleAppContainer
from twisted.web import static, server, resource, http
from os import path, popen, remove, stat

import json
import gzip
import cStringIO

from base import BaseController
from Components.config import config


class IpkgController(BaseController):

	def __init__(self, session, path = ""):
		BaseController.__init__(self, path=path, session=session)
		self.putChild('upload', IPKGUpload(self.session))

	def render(self, request):
		action =''
		package = ''
		self.request = request
		self.format = "html"
		self.container = None
		if "command" in request.args:
			action = request.args["command"][0]
		if "package" in request.args:
			package = request.args["package"][0]
		if "format" in request.args:
			self.format = request.args["format"][0]
		if action is not '':
			if action in ( "list", "list_installed", "list_upgradable", "update", "upgrade" ):
				return self.CallOPKG(request,action)
			elif action in ( "info", "status", "install", "remove" ):
				return self.CallOPKGP(request,action,package)
			elif action in ( "listgz" ):
				return self.CallOPKListGZ(request)
			elif action in ( "listall" ):
				return self.CallOPKListAll(request)
			elif action in ( "tmp" ):
				import glob
				tmpfiles = glob.glob('/tmp/*.ipk')
				ipks = []
				for tmpfile in tmpfiles:
					ipks.append({
						'path': tmpfile,
						'name' : (tmpfile.split('/')[-1]),
						'size' : stat(tmpfile).st_size,
						'date' : stat(tmpfile).st_mtime,
					})
				request.setHeader("content-type", "text/plain")
				request.write(json.dumps({'ipkfiles' : ipks}, encoding="ISO-8859-1"))
				request.finish()
				return server.NOT_DONE_YET
			else:
				return ShowError(request,"Unknown command: "+ self.command)
		else:
			return self.ShowHint(request)

		return ShowError(request,"Error")

	def CallOPKListGZ(self, request):
		tmpFilename = "/tmp/opkg-list.gz"
		if path.exists(tmpFilename):
			remove(tmpFilename)
		lines = popen('/usr/bin/opkg list | gzip > %s' % tmpFilename).readlines()
		request.setHeader("Content-Disposition", "attachment;filename=\"%s\"" % (tmpFilename.split('/')[-1]))
		rfile = static.File(tmpFilename, defaultType = "application/octet-stream")
		return rfile.render(request)

	def CallOPKListAll(self, request):
		data = self.getPackages()
		acceptHeaders = request.requestHeaders.getRawHeaders('Accept-Encoding', [])
		supported = ','.join(acceptHeaders).split(',')
		if 'gzip' in supported:
			encoding = request.responseHeaders.getRawHeaders('Content-Encoding')
			if encoding:
				encoding = '%s,gzip' % ','.join(encoding)
			else:
				encoding = 'gzip'
			request.responseHeaders.setRawHeaders('Content-Encoding',[encoding])
			compstr = self.compressBuf(json.dumps(data, encoding="ISO-8859-1"))
			request.setHeader('Content-Length', '%d' % len(compstr))
			request.write(compstr)
		else:
			request.setHeader("content-type", "text/plain")
			request.write(json.dumps(data, encoding="ISO-8859-1"))
			request.finish()

	def CallOPKG(self, request, action, parms=[]):
		cmd = ["/usr/bin/opkg", "ipkg", action] + parms
		request.setResponseCode(http.OK)
		self.ResultString = ''
		if hasattr(self.request, 'notifyFinish'):
			self.request.notifyFinish().addErrback(self.connectionError)
		self.container = eConsoleAppContainer()
		self.container.dataAvail.append(self.Moredata)
		self.container.appClosed.append(self.NoMoredata)
		self.IsAlive = True
		self.olddata = None
		self.container.execute(*cmd)
		return server.NOT_DONE_YET

	def getPackages(self):
		map = {}
		try:
			out = popen("opkg list")
			for line in out:
				if line[0] == " ":
					continue
				package = line.split(' - ')
				if map.has_key(package[0]):
					if map[package[0]][0] > package[1]:
						continue
				map.update( { package[0] : [ (package[1][:-1] if len(package) < 3 else package[1]),
					("" if len(package) < 3 else package[2][:-1]),
					 "0" , 
					 "0"] } )
			out = popen("opkg list-installed")
			for line in out:
				package = line.split(' - ')
				if map.has_key(package[0]):
					map[package[0]][2] = "1"
			out = popen("opkg list-upgradable")
			for line in out:
				package = line.split(' - ')
				if map.has_key(package[0]):
					map[package[0]][0] = package[1]
					map[package[0]][3] = package[2][:-1]
			keys=map.keys()
			keys.sort()
			ret = []
			for name in keys:
				ret.append({
				"name": name,
				"v": map[name][0],
				"d": map[name][1],
				"i": map[name][2],
				"u": map[name][3]
				})
			return ret
		except Exception, e:
			return []

	def connectionError(self, err):
		self.IsAlive = False

	def NoMoredata(self, data):
		if self.IsAlive:
			nresult=''
			for a in self.ResultString.split("\n"):
				#print "%s" % a
				if a.count(" - ") > 0:
					if nresult[:-1] == "\n":
						nresult+=a
					else:
						nresult+="\n" + a
				else:
					nresult+=a + "\n"
			nresult = nresult.replace("\n\n","\n")
			nresult = nresult.replace("\n "," ")
			if self.format == "json":
				data = []
				nresult=unicode(nresult, errors='ignore')
				data.append({"result": True,"packages": nresult.split("\n")})
				self.request.setHeader("content-type", "text/plain")
				self.request.write(json.dumps(data))
				self.request.finish()
			else:
				self.request.write("<html><body>\n")
				self.request.write(nresult.replace("\n", "<br>\n"))
				self.request.write("</body></html>\n")
				self.request.finish()

	def Moredata(self, data):
		if data != self.olddata or self.olddata is None and self.IsAlive:
			self.ResultString += data

	def CallOPKGP(self, request,action,pack):
		if pack is not '':
			return self.CallOPKG(request,action, [pack])
		else:
			return self.ShowError(request, "parameter: package is missing")

	def ShowError(self, request,text):
		request.setResponseCode(http.OK)
		request.write(text)
		request.finish()
		return server.NOT_DONE_YET

	def ShowHint(self, request):
		html = "<html><body><h1>OpenWebif Interface for OPKG</h1>"
		html += "Usage : ?command=<cmd>&package=packagename<&format=json><br>"
		html += "Valid Commands:<br>list,listgz,listall,list_installed,list_installed,list_upgradable<br>"
		html += "Valid Package Commands:<br>info,status,install,remove<br>"
		html += "Valid Formats:<br>json,html(default)<br>"
		html += "</body></html>"
		request.setResponseCode(http.OK)
		request.write(html)
		request.finish()
		return server.NOT_DONE_YET


class IPKGUpload(resource.Resource):
	def __init__(self, session):
		resource.Resource.__init__(self)
		self.session = session

	def mbasename(self, fname):
		l = fname.split('/')
		win = l[len(l)-1]
		l2 = win.split('\\')
		return l2[len(l2)-1]

	def render_POST(self, request):
		request.setResponseCode(http.OK)
		request.setHeader('content-type', 'text/plain')
		request.setHeader('charset', 'UTF-8')
		content = request.args['rfile'][0]
		filename = self.mbasename(request.args['filename'][0])
		if not content or not config.OpenWebif.allow_upload_ipk.value:
			result = [False,_('Error upload File')]
		else:
			if not filename.endswith(".ipk"):
				result = [False,_('wrong filetype')]
			else:
				import os
				FN = "/tmp/" + filename
				fileh = os.open(FN, os.O_WRONLY|os.O_CREAT )
				bytes = 0
				if fileh:
					bytes = os.write(fileh, content)
					os.close(fileh)
				if bytes <= 0:
					try:
						os.remove(FN)
					except OSError, oe:
						pass
					result = [False,_('Error writing File')]
				else:
					result = [True,FN]
		return json.dumps({"Result": result })
