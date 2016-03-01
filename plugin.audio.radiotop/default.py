#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2014 sorax
#
#  This file is part of the detektor.fm xbmc plugin.
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin.  If not, see <http://www.gnu.org/licenses/>.


from os.path import join
from sys import argv
from time import gmtime, strftime, strptime
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xml.dom.minidom import parseString
from xbmc import translatePath
import xbmcaddon
from xbmcgui import Dialog, ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

RADIOTOP_STREAM = 'http://193.105.67.24:8024'


class StreamPlayer:

    def __init__(self, url):
        self.url = url

    def addLink(self, name, url, image = 'http://www.radiotop.fm/rtfm.jpg', info = {}, totalItems = 0):
        item = ListItem(name.encode('utf-8'), iconImage = image, thumbnailImage = image)
        item.setProperty('mimetype', 'audio/mpeg')
        item.setInfo('music', info)
        return addDirectoryItem(int(argv[1]), url, item, False, totalItems)

    def buildIndex(self):
        self.addLink('[COLOR orange][B]RADIO TOP[/B][/COLOR] [COLOR blue] SLOVENIA [/COLOR]', self.url, 'http://www.radiotop.fm', {
            'title': 'Radio Top',
        })

    def run(self, handle):
        endOfDirectory(int(handle))

if __name__ == '__main__':
    radiotop = StreamPlayer(ROCKRADIO_STREAM)
    radiotop.buildIndex()
    radiotop.run(argv[1])
