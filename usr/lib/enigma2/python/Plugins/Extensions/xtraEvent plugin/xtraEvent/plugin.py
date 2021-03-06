# -*- coding: utf-8 -*-
# by digiteng...
# digiteng@gmail.com
# https://github.com/digiteng/
# 06.2020 - 08.2020
from __future__ import absolute_import
from Plugins.Plugin import PluginDescriptor
from Components.config import config
import threading
from . import xtra
from . import download


from six.moves import reload_module


def ddwn():
    download.save()
    if config.plugins.xtraEvent.timerMod.value == True:
        tmr = config.plugins.xtraEvent.timer.value
        t = threading.Timer(3600*int(tmr), ddwn) # 1h=3600
        t.start()
if config.plugins.xtraEvent.timerMod.value == True:
	threading.Timer(60, ddwn).start()


def main(session, **kwargs):
	reload_module(xtra)
	reload_module(download)

	try:
		session.open(xtra.xtra)
	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):
	return [PluginDescriptor(name="xtraEvent", description="xtraEvent plugin...", where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)]
