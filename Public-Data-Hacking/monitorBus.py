#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:49:10 2018

@author: neutron
"""
import urllib
from xml.etree.ElementTree import parse
candidates = ['1865', '1781','1397']
daveLat = 41.980262
def distance(lat1, lat2):
    return 69*abs(lat1 - lat2)

def monitor():
    u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
    doc = parse(u)
    for bus in doc.findall("bus"):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat,daveLat)
            print(busid, dis, 'miles')
           
            
import time
while True:
    monitor();
    print("-"*10)
    time.sleep(10)