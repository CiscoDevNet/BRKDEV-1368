#! /usr/bin/env python
"""
example-ssl.py
Illustrate the following concepts:
- Using requests to allow a self-signed certificate
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import requests
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Device Information
host = "ios-xe-mgmt.cisco.com"
port = "9443"
username = "root"
password = "D_Vay!_10&"

url = "https://{host}:{port}/.well-known/host-meta".format(host=host, port=port)

response = requests.get(url,
                        auth = (username, password),
                        verify = False
                       )

print(response.text)
