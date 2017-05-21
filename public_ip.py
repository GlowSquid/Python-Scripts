#!/usr/bin/python3

import requests

ip = requests.get("https://coralbeef.com/ip")
print(ip.text)
