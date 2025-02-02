# Cisco CSR1000v workshop online
#
# DevOps-MDP-01, 2022

import json
import requests

requests.packages.urllib3.disable_warnings()

api_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
    }

basicauth = ("developer", "C1sco12345")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback99",
        "description": "Whatever99",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "99.99.99.99",
                    "netmask": "255.255.255.0"
                    }
                ]
            },
        "ietf-ip:ipv6": {}
        }
    }

resp = requests.put(api_url, data = json.dumps(yangConfig), auth = basicauth, headers = headers, verify = False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print(f"STATUS OK: {resp.status_code}")
else:
    print(f"Error code {resp.status_code}, reply: {resp.json()}")


