#!/usr/bin/python
# -*- coding: utf-8 -*-
import gettext

from Components.Language import language
from Components.config import config as comp_config
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

LOCALES_DOMAIN = "OpenWebif"
LOCALES_RELPATH = "Extensions/OpenWebif/locale"

def _locale_init():
	gettext.bindtextdomain(
		LOCALES_DOMAIN,
		resolveFilename(SCOPE_PLUGINS, LOCALES_RELPATH))


def _(txt):
	try:
		t = gettext.dgettext(LOCALES_DOMAIN, txt)
		if t == txt:
			t = gettext.gettext(txt)
		return t
	except Exception:
		return txt


_locale_init()
language.addCallback(_locale_init)


try:
	AT_unit = comp_config.plugins.autotimer.unit.value == "hour" and _("hour") or _("minute")
except:  # noqa: E722
	AT_unit = "hour"

tstrings = {
	'mo': _("Mo"),
	'tu': _("Tu"),
	'we': _("We"),
	'th': _("Th"),
	'fr': _("Fr"),
	'sa': _("Sa"),
	'su': _("Su"),

	'day_0': _("Sun"),
	'day_1': _("Mon"),
	'day_2': _("Tue"),
	'day_3': _("Wed"),
	'day_4': _("Thu"),
	'day_5': _("Fri"),
	'day_6': _("Sat"),

	'monday': _("Monday"),
	'tuesday': _("Tuesday"),
	'wednesday': _("Wednesday"),
	'thursday': _("Thursday"),
	'friday': _("Friday"),
	'saturday': _("Saturday"),
	'sunday': _("Sunday"),

	'month_01': _("January"),
	'month_02': _("February"),
	'month_03': _("March"),
	'month_04': _("April"),
	'month_05': _("May"),
	'month_06': _("June"),
	'month_07': _("July"),
	'month_08': _("August"),
	'month_09': _("September"),
	'month_10': _("October"),
	'month_11': _("November"),
	'month_12': _("December"),

	'about': _("About"),
	'add_timer': _("Add Timer"),
	'add_autotimer': _("Add AutoTimer"),
	'add_zaptimer': _("Add Zap Timer"),
	'after_event': _("After Event"),
	'agc': _("AGC"),
	'all': _("All"),
	'all_channels': _("All Channels"),
	'authors': _("Authors"),
	'auto': _("Auto"),
	'back': _("Back"),
	'begin': _("Begin"),
	'ber': _("BER"),
	'bouquets': _("Bouquets"),
	'box': _("STB"),
	'box_info': _("STB info"),
	'box_uptime': _("STB uptime"),
	'boxcontrol': _("STB control"),
	'boxrctype': _("Factory RC type"),
	'brand': _("Brand/Meta"),
	'builddatestring': _("Build date"),
	'cancel': _("Cancel"),
	'capacity': _("Capacity"),
	'channel': _("Channel"),
	'channels': _("Channels"),
	'chipset': _("Chipset"),
	'cleanup_timer': _("Cleanup Timers"),
	'close': _("Close"),
	'contributors': _("Contributors"),
	'control': _("Control"),
	'cpu_arch': _("CPU architecture"),
	'cpu_benchmark': _("CPU benchmark"),
	'cpu_brand': _("CPU brand"),
	'current': _("Current"),
	'current_event': _("Current Event"),
	'date': _("Date"),
	'deep_standby': _("Deep-Standby"),
	'default': _("Default"),
	'delete': _("Delete"),
	'delete_recording': _("Delete Recording"),
	'delete_recording_question': _("Really delete the recording"),
	'delete_timer': _("Delete Timer"),
	'delete_timer_question': _("Really delete the timer"),
	'description': _("Description"),
	'developername': _("Compiled by"),
	'dhcp': _("DHCP"),
	'disable_timer': _("Disable Timer"),
	'disabled': _("disabled"),
	'displaytype': _("Display type"),
	'distro_version': _("Distro"),
	'dolby': _("Dolby"),
	'done': _("Done"),
	'download': _("Download"),
	'download_playlist': _("Download Playlist for"),
	'driver_date': _("Drivers"),
	'duration': _("Duration"),
	'dvb': _("DVB"),
	'dvbapi_type': _("DVB API"),
	'edit_timer': _("Edit Timer"),
	'enable_timer': _("Enable Timer"),
	'start': _("Start"),
	'end': _("End"),
	'enabled': _("Enabled"),
	'encrypted': _("Encrypted"),
	'enigmadebuglvl': _("Enigma2 debug level"),
	'enigmaver': _("Enigma2"),
	'epg': _("EPG"),
	'epgsearch': _("Epg Search"),
	'epgsearchextended': _("Include description"),
	'epgsearchbouquetsonly': _("Restrict to Bouquets"),
	'error': _("Error"),
	'every_timer': _("Every"),
	'extras': _("Extras"),
	'feedsurl': _("Feed URL"),
	'ffmpeg_version': _("FFmpeg"),
	'finished': _("finished"),
	'firmware_version': _("Image"),
	'flash_type': _("Flash type"),
	'fp_version': _("Frontprocessor"),
	'free': _("Free"),
	'free_memory': _("Free Memory"),
	'gateway': _("Gateway"),
	'grabscreenshot': _("Grab Screenshot"),
	'gstreamer_version': _("GStreamer"),
	'gui_version': _("GUI"),
	'havemultilib': _("MultiLib"),
	'hidefullremote': _("Hide full remote"),
	'high_resolution': _("High Resolution"),
	'hdd_model': _("Hard disk model"),
	'hour': _("Hour"),
	'hwserial': _("Hardware serial"),
	'imagearch': _("Image architecture"),
	'imagefilesystem': _("Image file system"),
	'imagefolder': _("Image folder"),
	'imagefpu': _("FPU"),
	'ipv4_address': _("IPv4 address"),
	'ipv4only_kernel': _("IPv4-only kernel"),
	'ipv4only_network': _("none/IPv4-only network"),
	'ipv4only_python': _("IPv4-only Python/Twisted"),
	'ipv6_address': _("IPv6 address(es)"),
	'info': _("Infos"),
	'instant_record': _("Instant Record"),
	'ask_instant_record': _("Really start instant record now?"),
	'javalib': _("Javascript Libraries"),
	'just_play': _("Just play"),
	'kernel_version': _("Kernel"),
	'lcd': _("LCD"),
	'license': _("LICENSE"),
	'loading': _("loading"),
	'location': _("Location"),
	'locked': _("Locked"),
	'mac_address': _("MAC address"),
	'main': _("Main"),
	'minute': _("Minute"),
	'model': _("Model"),
	'movielist': _("Movielist"),
	'movies': _("Movies"),
	'multi_epg': _("MultiEPG"),
	'multitranscoding': _("MultiTranscoding"),
	'name': _("Name"),
	'namespace': _("Namespace"),
	'network_interface': _("Network interface"),
	'no_description_available': _("no description available"),
	'not_implemented': _("Sorry this page is not yet implemented"),
	'nothing': _("Nothing"),
	'nothing_play': _("Nothing playing."),
	'now': _("Now"),
	'oe_version': _("OE"),
	'on': _("On"),
	'openwebif_header': _("Open Source Web Interface for Linux set-top box"),
	'openvision': _("Open Vision"),
	'ovrctype': _("Open Vision RC type"),
	'ovrcname': _("Open Vision RC name"),
	'ovrcidnum': _("Open Vision RC ID number"),
	'show_boxname': _("Show STB name in header"),
	'use_custom_boxname': _("Use custom STB name"),
	'custom_boxname': _("Custom STB name"),
	'osd': _("OSD"),
	'open_in_new_window': _("Open in new window"),
	'pip': _("PiP"),
	'platform': _("Platform"),
	'playback': _("Playback"),
	'playlist': _("Playlist"),
	'powercontrol': _("Power Control"),
	'procmodel': _("Proc model"),
	'procmodeltype': _("Hardware type"),
	'provider': _("Provider"),
	'providers': _("Providers"),
	'python_version': _("Python"),
	'radio': _("Radio"),
	'reboot_box': _("Reboot STB"),
	'rec_status': _("Recording Status"),
	'refresh': _("Refresh"),
	'refresh_auto': _("Refresh automatically every"),
	'refresh_timer': _("Refresh Timer"),
	'remote': _("Remote"),
	'rename_recording': _("Rename Recording"),
	'rename_recording_question': _("Really rename the recording"),
	'repeated': _("Repeated"),
	'restart_gui': _("Restart GUI"),
	'running': _("running"),
	'safe_mode': _("Safe mode"),
	'satellites': _("Satellites"),
	'satfinder': _("Satfinder"),
	'save': _("Save"),
	'screenshot': _("Screenshot"),
	'search': _("Search"),
	'search_csfd': _("Search CSFD"),
	'search_imdb': _("Search IMDb"),
	'search_kinopoisk': _("Search KinoPoisk"),
	'seconds': _("seconds"),
	'send_message': _("Send Message"),
	'sent_wait': _('Waiting for answer ...'),
	'sendamessage': _("Send a Message"),
	'service': _("Service"),
	'settings': _("Settings"),
	'Bouquet_Editor': _("Bouquet Editor"),
	'shiftforlong': _("(Shift + Click for Long Press)"),
	'show_full_openwebif': _("Show Full OpenWebif"),
	'showfullremote': _("Show full remote"),
	'show_epg_for': _("Show EPG for"),
	'shutdown': _("Shutdown"),
	'site_source': _("Site and sources"),
	'snr': _("SNR"),
	'soc_family': _("SoC family"),
	'software': _("Software"),
	'standby': _("Standby"),
	'standby_toggle': _("Standby Toggle"),
	'wake_up': _("Wake Up"),
	'start_after_end': _("Start time is after end time"),
	'start_instant_record': _("Start Instant Record"),
	'stream': _("Stream"),
	'subnet_mask': _("Subnet mask"),
	'subservices': _("Subservices"),
	'tags': _("Tags"),
	'teletext': _("Teletext"),
	'television': _("Television"),
	'template_engine': _("Template Engine"),
	'text': _("Text"),
	'time': _("Time"),
	'timeout': _("Timeout"),
	'timer_added': _("Timer added"),
	'timer_list': _("Timerlist"),
	'timer_newname': _("New Name"),
	'timer_preview': _("Autotimer Preview"),
	'timer': _("Timer"),
	'timers': _("Timers"),
	'title': _("Title"),
	'main_memory': _("Free/Total memory"),
	'transcoded': _("transcoded"),
	'transcode': _("Transcode"),
	'transcoding': _("Transcoding"),
	'tuner_ber': _("Tuner Bit Error Rate BER"),
	'tuner_number': _("Tuner Number"),
	'tuner_signal': _("Tuner Signal"),
	'tuner_signal_snr': _("Tuner Signal Quality SNR"),
	'tuner_signal_snr_db': _("Tuner Signal Quality SNR_DB"),
	'tuner_signal_agc': _("Tuner Signal Power AGC"),
	'tuner_type': _("Tuner Type"),
	'tuners': _("Tuners"),
	'tv': _("TV"),
	'tv_multi_epg': _("TV Multi EPG"),
	'type': _("Type"),
	'upcoming_events': _("Upcoming Events"),
	'updatedatestring': _("Last update"),
	'version': _("Version"),
	'video': _("Video"),
	'video_height': _("Video Height"),
	'video_wide': _("Video Wide"),
	'video_width': _("Video Width"),
	'vision_module': _("Open Vision module"),
	'vision_revision': _("Open Vision revision"),
	'vision_version': _("Open Vision version"),
	'vps': _("VPS"),
	'volume': _("Volume"),
	'volumecontrol': _("Volume Control"),
	'waiting': _("waiting"),
	'warning': _("Warning"),
	'yes_no': _("Yes/No"),
	'zap': _("Zap"),
	'zapbeforestream': _("zap before Stream"),
	'zap_to': _("Zap to"),
	'zapped_to': _("Zapped to"),
	'translation_spanish': _('Translation to Spanish'),
	'license_text': _('All Files of this Software are open source software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.'),
	'Root': _('Root'),

	'at_list': _("AutoTimer List"),
	'at_at_edit': _("AutoTimer Edit"),
	'at_enabled': _("Enabled"),
	'at_description': _("Description"),
	'at_title_match': _("Match title"),
	'at_encoding': _("EPG encoding"),
	'at_search_type': _("Search type"),
	'at_partial_match': _("partial match"),
	'at_exact_match': _("exact match"),
	'at_description_match': _("description match"),
	'at_title_or_description_match': _("title or description match"),
	'at_title_or_short_description_match': _("title or short description match"),
	'at_short_description_match': _("short description match"),
	'at_start_match': _("start match"),
	'at_search_strictness': _("Search strictness"),
	'at_case_sensitive': _("case-sensitive search"),
	'at_case_insensitive': _("case-insensitive search"),
	'at_timer_type': _("Timer type"),
	'at_record': _("record"),
	'at_zap': _("zap"),
	'at_override_alt': _("Override found with alternative service"),
	'at_timespan': _("Only match during timespan"),
	'at_timespan_begin': _("Begin of timespan"),
	'at_timespan_end': _("End of Timespan"),
	'at_datespan': _("Restrict to events on certain dates"),
	'at_datespan_after': _("Not after"),
	'at_datespan_before': _("Not before"),
	'at_timer_offset': _("Custom offset"),
	'at_timer_offset_before': _("Offset before recording (in m)"),
	'at_timer_offset_after': _("Offset after recording (in m)"),
	'at_max_duration': _("Set maximum duration"),
	'at_after_event': _("After event"),
	'at_after_event_standard': _("standard"),
	'at_after_event_auto': _("auto"),
	'at_after_event_nothing': _("do nothing"),
	'at_after_event_standby': _("go to standby"),
	'at_after_event_deepstandby': _("go to deep standby"),
	'at_event_timespan': _('Execute "after event" during timespan'),
	'at_event_timespan_begin': _('Begin of "after event" timespan'),
	'at_event_timespan_end': _('End of "after event" timespan'),
	'at_max_counter': _("Record a maximum of x times"),
	'at_left': _("Amount of recordings left"),
	'at_never': _("Never"),
	'at_monthly': _("Monthly"),
	'at_weekly_sun': _("Weekly (Sunday)"),
	'at_weekly_mon': _("Weekly (Monday)"),
	'at_reset_count': _("Reset count"),
	'at_avoid_dup': _("Require description to be unique"),
	'at_avoid_dup_no': _("No"),
	'at_avoid_dup_same_service': _("On same service"),
	'at_avoid_dup_any_service': _("On any service"),
	'at_avoid_dup_any_service_rec': _("Any service/recording"),
	'at_location': _("Use a custom location"),
	'at_tags': _("Tags"),
	'at_select_tags': _("select Tags"),
	'at_channels': _("Channels"),
	'at_select_channels': _("select Channels"),
	'at_bouquets': _("Bouquets"),
	'at_select_bouquets': _("select Bouquets"),
	'at_filter': _("Enable Filtering"),
	'at_filter_include': _("Include"),
	'at_filter_exclude': _("Exclude"),
	'at_filter_title': _("in Title"),
	'at_filter_short_desc': _("in Shortdescription"),
	'at_filter_desc': _("in Description"),
	'at_filter_day': _("on Weekday"),
	'at_filter_weekend': _("Weekend"),
	'at_filter_weekday': _("Weekday"),
	'at_add': _("Add"),
	'at_del': _("Delete"),
	'at_reload': _("Reload"),
	'at_save': _("Save"),
	'at_parse': _("Parse"),
	'at_simulate': _("Simulate"),
	'at_timers': _("Timers"),
	'at_settings': _("Settings"),
	'at_delete_autotimer_question': _("Do you really want to delete the AT"),
	'at_label_series': _("Label series"),

	'ats_auto_timer_settings': _("AutoTimer Settings"),
	'ats_autopoll': _("AutoPoll"),
	'ats_interval': _("Interval (in %s)") % AT_unit,
	'ats_maxdaysinfuture': _("Max Days"),
	'ats_try_guessing': _("Try Guessing"),
	'ats_fastscan': _("Fastscan"),
	'ats_show_in_extensionsmenu': _("Show in Extensionsmenu"),
	'ats_disabled_on_conflict': _("Disabled on Conflict"),
	'ats_addsimilar_on_conflict': _("Add Similar on Conflict"),
	'ats_notifconflict': _("Notify if Conflict"),
	'ats_notifsimilar': _("Notify if Similar"),
	'ats_add_autotimer_to_tags': _("Add Autotimer to Tags"),
	'ats_add_name_to_tags': _("Add Name to Tags"),
	'ats_refresh': _("Refresh"),
	'ats_refresh_none': _("None"),
	'ats_refresh_auto': _("Auto"),
	'ats_refresh_all': _("All"),
	'ats_editor': _("Editor"),
	'ats_editor_plain': _("Plain"),
	'ats_editor_wizzard': _("Wizzard"),

	'er_enabled': _("Enabled"),
	'er_enable_messages': _("Enable Messages"),
	'er_begin': _("Begin"),
	'er_end': _("End"),
	'er_delay_standby': _("Delay Standby"),
	'er_interval_min': _("Interval (min.)"),
	'er_interval_sec': _("Interval (sec.)"),
	'er_afterevent': _("After Event"),
	'er_force': _("Force"),
	'er_wakeup': _("Wakeup"),
	'er_inherit_autotimer': _("Inherit Autotimer"),
	'er_parse_autotimer': _("Parse Autotimer"),
	'er_always': _("Always"),
	'er_never': _("Never"),
	'er_bg_only': _("Background only"),
	'er_ask_yes': _("Ask, default Yes"),
	'er_ask_no': _("Ask, default No"),
	'er_adapter': _("Method"),
	'er_main': _("Visibly"),
	'er_pip': _("Picture in Picture"),
	'er_pip_hidden': _("Picture in Picture (hidden)"),
	'er_fake_recording': _("Fake Recording"),
	'er_reload': _("Reload"),
	'er_save': _("Save"),
	'er_refresh': _("Refresh now"),

	'bqe_add_provider_as_bouquet': _("Add Provider as new Bouquet"),
	'bqe_add_channel': _("Add channel(s) to Bouquet"),
	'bqe_add_alternative': _("Add channel(s) as alternate"),
	'bqe_search': _("Search"),
	'bqe_reload': _("Reload"),
	'bqe_add_bq': _("Add Bouquet"),
	'bqe_rename_bq': _("Rename Bouquet"),
	'bqe_delete_bq': _("Delete Bouquet"),
	'bqe_add_marker': _("Add Marker"),
	'bqe_add_spacer': _("Add Spacer"),
	'bqe_rename': _("Rename"),
	'bqe_del_channel_question': _("Do you really want to delete the selected item(s)"),
	'bqe_del_bouquet_question': _("Do you really want to delete the bouquet"),
	'bqe_name_bouquet': _("Name of the Bouquet"),
	'bqe_name_marker': _("Name of the Marker"),
	'bqe_rename_bouquet': _("Enter new name for the bouquet"),
	'bqe_rename_marker': _("Enter new name for the marker"),
	'bqe_filename': _("Please enter filename"),
	'bqe_restore_question': _("Do you really want to restore from file"),

	'via': _("via"),
	'record_zap': _("Record+ZAP"),
	'pmt_pid': _("Pmtpid"),
	'a_pid': _("Apid"),
	'v_pid': _("Vpid"),
	'pcr_pid': _("Pcrpid"),
	'ts_id': _("Tsid"),
	'on_id': _("Onid"),
	's_id': _("Sid"),
	's_ref': _("Sref"),
	's_orb': _("Orbital Position"),

	'tstr_error_load_page': _("error! Loading Page"),
	'tstr_timer_added': _("Timer Added"),
	'tstr_event_not_found': _("Event not found"),
	'tstr_show_picon_in_channel_list': _("Show Picon in channel list"),
	'tstr_moviedb': _("Movie database for EPG"),

	'tstr_ow_browser_settings': _("OpenWebif Browser Settings"),
	'tstr_ow_settings': _("OpenWebif Settings"),
	'tstr_theme': _("Theme"),
	'tstr_spinner': _("Spinner"),
	'display_duration_s': _("Display duration (s)"),

	'display_mode': _("Display Mode"),
	'tv_guide': _("TV Guide"),
	'timeline': _("Timeline"),
	'webtv': _("Web TV"),
	'cw': _("Calendar Week"),

	'linkspeed': _("Link speed"),
	'networkshares': _("Network Shares"),
	'using': _("using"),
	'prime_times': _("Primetimes"),
	'titscreenshot': _("Enable/Disable Screenshot on key press or"),

	'bookmarks': _("Bookmarks"),
	'bookmark': _("Bookmark"),
	'delete_bookmark': _("Delete Bookmark"),

	'packages': _("Packages"),

	'newdesign': _('Use new design'),
	'no_cancel': _("No, cancel"),
	'yes_delete': _("Yes, delete it"),
	'cancelled': _("Cancelled"),
	'deleted': _("Deleted"),
	'need_input': _("You need to write something!"),
	'common_settings': _("Common Settings"),
	'min_movie_list': _("Minimal movie list"),
	'min_timer_list': _("Minimal timer list"),
	'min_epg_list': _("Minimal EPG list"),
	'remove_package': _("Remove Package"),
	'update_package': _("Update Package"),
	'install_package': _("Install Package"),
	'update': _("Update"),
	'installed': _("Installed"),
	'more': _("More"),
	'update_feed': _("Update from Feed"),
	'upgrade_packages': _("Upgrade all Packages"),
	'yes': _("Yes"),
	'inc_shortdesc': _("Include short description"),
	'inc_extdesc': _("Include extended description"),
	'moviesearch': _("Movie search"),
	'start_typing': _("START TYPING"),
	'select_ipk_upload': _("Select IPK File for Upload"),
	'uploaded_files': _("Uploaded Files"),
	'upload_package': _("Upload package"),
	'upload_error': _("Upload File Error"),
	'showfullremoteshort': _("Full remote"),
	'showdetails': _("Show details"),
	'show_details_in_channel_list': _("Show Service type in channel list"),
	'export': _("Export"),
	'import': _("Import"),

	'playlistformat': _("Playlist Format"),
	'pipifposible': _("Use as PiP if possible"),
	'allow_duplicate': _("Allow duplicates"),
	'autoadjust': _("Adjust recording time to real event time"),
	'avoidDuplicateMovies': _("Don't create timer when movie exists in database"),

	'streamclients': _("Stream Clients")
}
