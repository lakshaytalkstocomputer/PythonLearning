#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:08:21 2018

@author: neutron
"""

daveLat = 41.980262

from xml.etree.ElementTree import parse

doc = parse("rt22.xml")
for bus in doc.findall("bus"):
    lat=float(bus.findtext("lat"))
    if lat > daveLat:
        direction = bus.findtext('d')
        if direction.startswith("North"):
            busid = bus.findtext("id")
            print(busid, lat)