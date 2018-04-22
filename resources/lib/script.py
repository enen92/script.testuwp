# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
import logging
import xbmcaddon
import xbmcgui
import xbmc


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))


# Put your code here, this is just an example showing
# a textbox as soon as this addon gets called
def show_dialog():
    addon_name = ADDON.getAddonInfo('name')

    line1 = "Is UWP = %s" % bool(xbmc.getCondVisibility("system.platform.uwp"))

    xbmcgui.Dialog().ok(addon_name, line1)
