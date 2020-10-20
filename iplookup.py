import re
import json
import urllib
import urllib.parse
import urllib.request
from urllib.request import Request, urlopen

wp = urllib.request.urlopen("http://example.com")

pw = wp.read()

print(pw)

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print ('détail de votre ip :\n ')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
