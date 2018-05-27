#!/usr/bin/python3

import requests

domain = ".ns.agency"


sub = "gov"


url = "https://" + sub + domain



r = requests.get(url)

if(r.status_code != 404):
    print(url)
    print(r.status_code)
