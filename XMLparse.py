import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from xml.etree.ElementTree import parse
api_key = False
import ssl
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


x=input('Link')
url=urlopen(x).read()

st=ET.fromstring(url)
lst=st.findall('.//count')
sum=0
for line in lst:
    sum+=int(line.text)
print(sum)
