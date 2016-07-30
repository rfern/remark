# Load Car Ownership
#
# ABS provides some car ownership data, this can be used to develop secondary metrics.
# This script downloads and converts this data to JSON with suburb centrioid coords.



import urllib.request
import xml.etree.ElementTree as ET
import csv

# Data from ABS:
# dataset: ABS_CENSUS2011_B29
# filter:  TOT+0_4+0+1+2+3+4+Z.D.+.SA2.+.A
dataset = "http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_CENSUS2011_B29/TOT+0_4+0+1+2+3+4+Z.D.+.SA2.+.A/ABS?startTime=2011&endTime=2011"


# Download:
response = urllib.request.urlopen(dataset)
data = response.read()
data = data.decode('utf-8')

# Read XML from ABS
root = ET.fromstring(data)

for statData in root.findall('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Series'):
	region = statData.find('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Value/[@concept="REGION"]').attrib['value']
	value = statData.find('.//{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}ObsValue/[@value]').attrib['value']
	print(region + ',' + value)