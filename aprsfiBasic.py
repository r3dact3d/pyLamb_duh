e!/usr/bin/env python
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
    result = request.json()
    if result['result'] == 'ok':
        print(result['entries'])
    else:
        print(result)
else:
    print('An error has occured with the request.')
