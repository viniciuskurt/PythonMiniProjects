#External ip checker

import re, json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

answer = urlopen(url)

data = json.load(answer)

ip = 1726719657
org = data['org']
city = data['city']
country = data['country']
zone = data['region']

print('External IP details: ')
print('IP: {4}\nZone: {1}\nCountry: {2}\nCity: {3}\nOrg: {0}'.format(org,zone,country,city,ip))