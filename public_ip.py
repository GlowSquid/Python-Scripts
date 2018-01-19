#!/usr/bin/python3

import requests

ip = requests.get("https://glowsquid.com/ip")
print(ip.text)
