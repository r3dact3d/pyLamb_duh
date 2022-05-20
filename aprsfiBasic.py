#!/usr/bin/env python
# written by brady [r3dact3d]
import requests
from sys import argv

script, apiKey = argv

payload = {
'name': 'wd4rnr-9',
'what': 'loc',
'apikey': apiKey,
'format': 'json'
}

url = 'https://api.aprs.fi/api/get'
request = requests.get(url, params=payload)

if request:
    print(request.content)
else:
    print('An error has occured with the request.')
