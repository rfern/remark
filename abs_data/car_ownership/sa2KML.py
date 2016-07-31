import zipfile
import json
import csv
import io
import urllib.request
import csv
from fastkml import kml
from random import randint
import re
import json
import math

## Get SA2 Map from ABS ##

url = "http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/4B80C5D126524576CA257B3B001A69C6/$File/2033.0.55.001%20irsad%20sa2.zip"
response = urllib.request.urlopen(url)
ZIPResp = response.read()
ZIPStrm = io.BytesIO(ZIPResp)
ZIPFile = zipfile.ZipFile(ZIPStrm)
KMZFile = ZIPFile.open(ZIPFile.namelist()[0])
KMZFile = KMZFile.read()

KMZStrm = io.BytesIO(KMZFile)
KMZZip  = zipfile.ZipFile(KMZStrm)
KMLFile = KMZZip.open('doc.kml')
KMLData = KMLFile.read().decode()

## Fix KML for fastKML

invalidKML = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document id="2011 IRSAD - SA2" xsi:schemaLocation="http://www.opengis.net/kml/2.2 http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd http://www.google.com/kml/ext/2.2 http://code.google.com/apis/kml/schema/kml22gx.xsd">"""

validKML = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>"""

KMLData = KMLData.replace(invalidKML, validKML)
KMLData = KMLData.replace('2011 IRSAD - SA2', '2011 B29 - Cars per SQKM')

## Load the KML

KMLFile = kml.KML()
KMLFile.from_string(KMLData)

SA2Styles = list(list(KMLFile.features())[0].styles())
SA2Folder = list(list(list(KMLFile.features())[0].features())[0].features())

## Add our colours

colours = ['000d660b', '000d660b', 'ff189815', 'ff27ca98', 'ff38feff', 'ff2dc1fe', 'ff279afe', 'ff1b0dfd', 'ff1006b3', 'ff1006b3']

for style in zip(SA2Styles, colours):
	style[0]._styles[1].color = style[1]


## Search for SA codes

SA2CodeRE = re.compile('SA2 Code</td>\n<td>([0-9]*)')

## Load Data for car ownership

with open('carOwnershipData.json', 'r') as carOwnershipFP:
	regionData = json.load(carOwnershipFP)

## Calculate max cars per SQ KM

maxCarsPerKM = 0
for region in regionData:
	# First use the average
	regionData[region]['carsperkm'] = float(regionData[region]['TotalCars']) / 3448.39738;

	# if region size is zero
	if 'Size' in regionData[region]:
		if float(regionData[region]['Size']) > 0:
			regionData[region]['carsperkm'] = float(regionData[region]['TotalCars'])/float(regionData[region]['Size'])

	regionData[region]['carsperkm'] = math.log(regionData[region]['carsperkm']+1)

	if regionData[region]['carsperkm'] > maxCarsPerKM:
		maxCarsPerKM = regionData[region]['carsperkm']

## Update KML

nStyles = len(SA2Styles)-1
for region in SA2Folder:
	SA2Code = SA2CodeRE.findall(region.description)[0]
	SA2Color = int(round((regionData[SA2Code]['carsperkm']/maxCarsPerKM)*(nStyles-1),0))
	SA2Color = min(SA2Color, nStyles-1)
	region._styleUrl = SA2Styles[SA2Color]
	region.description = "Region has {} cars, with {} cars per skm, color goes to {}".format(regionData[SA2Code]['TotalCars'],str(regionData[SA2Code]['carsperkm']),str(SA2Color))

with open('test.kml', 'w') as KMLOutFile:
	KMLOutFile.write(KMLFile.to_string())
