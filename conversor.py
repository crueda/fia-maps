#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# autor: Carlos Rueda
# fecha: 2013-04-03
# mail: carlos.rueda@deimos-space.com

import datetime
import time
import os
import sys
import csv
import logging, logging.handlers
import httplib
import urllib
import urllib2
import math

def degrees2meters(lon,lat):
        x = lon * 20037508.34 / 180;
        y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180);
        y = y * 20037508.34 / 180;
        return [x, y]

def meters2degree(x, y):
 	lon = (x / 20037508.34) * 180
 	lat = (y / 20037508.34) * 180
 	lat = 180/math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
	return [lon, lat]

def toMercator(lat,lon):
	x = lon * 20037508.34 / 180
	y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
	y = y * 20037508.34 / 180
	return [y, x]

def inverseMercator (x, y):
 	lon = (x / 20037508.34) * 180
 	lat = (y / 20037508.34) * 180
 	lat = 180/math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
	return [lat, lon]

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)


lon = -3.2314
lat = 41.23145

print str(lat) + "," + str(lon)

result1 = degrees2meters(lon,lat)
print result1
result2 = meters2degree(result1[0],result1[1])
print result2

print "-----"
#y=4422340.704086
#x=-763147.2938515

y=-947819.15415541
x=4526906.5587614

y=-948889.27255121
x=4527059.4328179

y=-899042.061427
x=4431114.91748


result = meters2degree(x,y)
print str(result[1])+","+str(result[0])

#result1 = toMercator(lat,lon)
#print result1
#result2 = inverseMercator(result1[0],result1[1])
#print result2

#print deg2num(lat,lon,16)