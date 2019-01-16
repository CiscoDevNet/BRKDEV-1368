#! /usr/bin/env python
"""
<<<<<<< HEAD
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Hank Preston <hapresto@cisco.com>"
__contributors__ = "Bryan Byrne <brybyrne@cisco.com>"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"
=======
Learning Series: Network Programmability Basics
Author: Hank Preston <hapresto@cisco.com>

device_info.py
Illustrate the following concepts:
- Store device info for Sandbox Infrastructure used 
  in examples
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"
>>>>>>> master

# DevNet Always-On NETCONF/YANG & RESTCONF Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "ios-xe-mgmt.cisco.com",
<<<<<<< HEAD
             "port": 9443,
=======
             "port": 10000,
>>>>>>> master
             "username": "root",
             "password": "D_Vay!_10&"
          }

# DevNet IOS XE Programmability Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/7fd27b24-7034-477d-9ad2-e2c8096dd1a5?diagramType=Topology
ios_xe2 = {
             "address": "10.10.20.21",
<<<<<<< HEAD
             "port": 9443,
             "username": "root",
             "password": "cisco123"
          }
=======
             "port": 830,
             "username": "root",
             "password": "cisco123"
          }


# DevNet Always-On Sandbox APIC-EM
# https://devnetsandbox.cisco.com/RM/Diagram/Index/2e0f9525-5f46-4f46-973e-0f0c1bf934fa?diagramType=Topology
apicem = {
             "host": "sandboxapicem.cisco.com",
             "username": "devnetuser",
             "password": "Cisco123!",
             "port": 443
         }

# DevNet Always-On Sandbox ACI APIC
# https://devnetsandbox.cisco.com/RM/Diagram/Index/5a229a7c-95d5-4cfd-a651-5ee9bc1b30e2?diagramType=Topology
apic = {
             "host": "https://sandboxapicdc.cisco.com",
             "username": "admin",
             "password": "ciscopsdt",
             "port": 443
         }

>>>>>>> master
