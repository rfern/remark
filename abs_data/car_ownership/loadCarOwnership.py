# Load Car Ownership
#
# ABS provides some car ownership data, this can be used to develop secondary metrics.
# This script downloads and converts this data to JSON with suburb centrioid coords.


import zipfile
import urllib.request
import json
import csv
import io
import xml.etree.ElementTree as ET
import urllib.request
import csv
import math

## Get Location 

def arcgizKMZ(location):
	baseURL = 'http://censusdata.abs.gov.au/arcgis/rest/services/ASGS2016/SA2/MapServer/1/query?'
	query = ['text='+location,
			 'geometry=',
			 'geometryType=esriGeometryEnvelope',
			 'inSR=',
			 'spatialRel=esriSpatialRelIntersects',
			 'relationParam=',
			 'objectIds=',
			 'where=',
			 'time=',
			 'returnCountOnly=false',
			 'returnIdsOnly=false',
			 'returnGeometry=true',
			 'maxAllowableOffset=',
			 'outSR=',
			 'outFields=',
			 'f=kmz']
	query = "&".join(query)

	url = baseURL + query

	response = urllib.request.urlopen(url)
	KMZFile = response.read()
	KMZFile = io.BytesIO(KMZFile)
	KMZZip  = zipfile.ZipFile(KMZFile)
	KMLFile = KMZZip.open('doc.kml')
	KMLData = KMLFile.read().decode()

	KMLDoc = ET.fromstring(KMLData)

	latlong = KMLDoc.find('.//{http://www.opengis.net/kml/2.2}coordinates').text
	latlong = latlong.split(',')
	latlong = dict({'lng': latlong[1], 'lat': latlong[0]})

	return latlong

# Data from ABS:
# dataset: ABS_CENSUS2011_B29
# filter:  TOT+0_4+0+1+2+3+4+Z.D.+.SA2.+.A
dataset = "http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_CENSUS2011_B29/TOT.D.+.SA2.+.A/ABS?startTime=2011&endTime=2011"


# Download:
response = urllib.request.urlopen(dataset)
data = response.read()
data = data.decode('utf-8')

# Load census data
root = ET.fromstring(data)

regionData = {}
for statData in root.findall('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Series'):
	region = statData.find('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Value/[@concept="REGION"]').attrib['value']
	value = statData.find('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}ObsValue/[@value]').attrib['value']
	metric = statData.find('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Value/[@concept="MEASURE"]').attrib['value']

	regionData[region] = {'TotalCars': value}

## Get region sizes from area information
with open('SA2_2016_AUST.csv', 'r') as csvfile:
	csvfile.readline()
	dataReader = csv.reader(csvfile)
	for row in dataReader:
		if row[0] in regionData:
			regionData[row[0]].update({'Suburb': row[2], 'State': row[10], 'Size': row[11]})

## Get Lat Lon of region
for region in regionData:
	try:
		regionData[region].update(arcgizKMZ(region))
	except:
		pass

	print(regionData[region])

with open('carOwnershipData.json', 'w') as outfile:
    json.dump(regionData, outfile)

# "TotalCars": "5405", "Size": "13.0112", "lng": "-27.605757", "State": "Queensland", "lat": " 153.145906", "Suburb": "Rochedale South - Priestdale"
with open('carOwnershipData.csv', 'w') as outfile:
	outfile.write('TotalCars,Size,State,Suburb,lat,lng,CarsPerSQKM\n')
	for region in regionData:
		try:
			cols = [regionData[region]['TotalCars'], regionData[region]['Size'], regionData[region]['State'], regionData[region]['Suburb'],
			 regionData[region]['lat'], regionData[region]['lng'], float(regionData[region]['TotalCars'])/float(regionData[region]['Size'])]

			if math.isnan(cols[-1]):
			 	cols[-1] = 0

			cols[-1] = str(cols[-1])

			line = ",".join(cols)

			outfile.write(line+'\n')
		except:
			pass
