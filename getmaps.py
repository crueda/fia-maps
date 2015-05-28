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


########################################################################
LOG = "./getmaps.log"
LOG_FOR_ROTATE = 10

lat_min = 36.929
lat_max = 37.627
lon_min = -8.520
lon_max = -7.792

meters = 100

########################################################################

########################################################################
# definicion y configuracion de logs
try:
    logger = logging.getLogger('getmaps')
    loggerHandler = logging.handlers.TimedRotatingFileHandler(LOG , 'midnight', 1, backupCount=LOG_FOR_ROTATE)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    loggerHandler.setFormatter(formatter)
    logger.addHandler(loggerHandler)
    logger.setLevel(logging.DEBUG)
except Exception, error:
    print '------------------------------------------------------------------'
    print '[ERROR] Error writing log at %s' % error
    print '------------------------------------------------------------------'
    exit()
########################################################################

def degrees2meters(lat,lon):
	x = lon * 20037508.34 / 180
	y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
	y = y * 20037508.34 / 180
	return [y, x]

logger.info("START")

pointA = [lat_min, lon_min]
pointB = [lat_max, lon_max]
pointA_conv = degrees2meters(lat_min, lon_min)
pointB_conv = degrees2meters(lat_max, lon_max)
lat_min_conv = pointA_conv[0]
lon_min_conv = pointA_conv[1]
lat_max_conv = pointB_conv[0]
lon_max_conv = pointB_conv[1]

url = "http://89.140.246.28:6969/cgi-bin/mapserv.fcgi?map=/var/www/external/external.map&LAYERS=osm2&SPHERICALMERCATOR=true&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&FORMAT=image%2Fjpeg&SRS=EPSG%3A900913&WIDTH=256&HEIGHT=256"

lat = lat_min_conv
while (lat < lat_max_conv):
	lon = lon_min_conv
	while (lon < lon_max_conv):	
		bbox = "&BBOX="+str(lon-meters)+","+str(lat-meters)+","+str(lon+meters)+","+str(lat+meters)
		logger.info(url+bbox)      
		urllib.urlopen(url+bbox)
		lon = lon + meters
	lat = lat + meters

logger.info("DONE!")

