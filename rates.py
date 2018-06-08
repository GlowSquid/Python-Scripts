#!/usr/bin/python3

import requests
import json

# Using fixer.io
# r = requests.get("https://api.fixer.io/latest?base=EUR&symbols=NOK") # Old way. No more HTTPS encryption or extended currencies without subscription..
# r = requests.get("http://data.fixer.io/api/latest?access_key=<YOUR_API>&base=EUR&symbols=NOK") # New way

# Using exchangeratesapi.io
r = requests.get("https://exchangeratesapi.io/api/latest?base=EUR&symbols=NOK")

resp = json.loads(r.text)
print (resp["base"], resp["rates"]["NOK"])
