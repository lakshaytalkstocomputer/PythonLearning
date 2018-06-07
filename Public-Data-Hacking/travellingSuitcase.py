#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:37:05 2018

@author: neutron
"""

import urllib
u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data = u.read()
f = open("rt22.xml", "wb")
f.write(data)
f.close()