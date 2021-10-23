# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/wreckagesystems
#------------------------------------------------------------
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.wreckagesystems'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

URL1 = "https://wreckage-systems.club/radio/8000/radio.mp3"
URL2 = "https://wreckage-systems.club/radio/8000/stream192.mp3"
YOUTUBE_CHANNEL_ID = "65propaganda"

# Entry point
def run():
    plugintools.log("wreckagesystems.run")
    # Get params
    params = plugintools.get_params()
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("wreckagesystems.main_list "+repr(params))
#note below - some YTs are /user/xxx and some /channel/xxx
    plugintools.add_item(
        #action="",
        title="Wreckage Systems",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )
        {
            'label': plugin.get_string(30001),
            'path': "https://wreckage-systems.club/radio/8000/radio.mp3",
            'thumbnail': "https://github.com/leopheard/WreckageSystems/blob/master/resources/media/65_alt_square.gif?raw=true",
            'is_playable': True},
        {
            'label': plugin.get_string(30002),
            'path': "https://wreckage-systems.club/radio/8000/stream192.mp3",
            'thumbnail': "https://github.com/leopheard/WreckageSystems/blob/master/resources/media/65_alt_square.gif?raw=true",
            'is_playable': True},
run()
