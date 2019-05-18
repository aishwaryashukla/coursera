import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import pprint

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_231628.xml'  # input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
# url = serviceurl + urllib.parse.urlencode(parms)
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context = ctx)

data = uh.read()
# pprint.pprint(data)
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)
count_all = 0
for elem in tree[1]:
    # print(elem.find('count').text)
    count_all += int(elem.find('count').text)
    # print(elem.findall)
results = tree.findall('commentinfo')
print("Total count is : {}".format(count_all))
