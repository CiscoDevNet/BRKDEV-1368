#! /usr/bin/env python
"""
Cisco Live BRKDEV-1368:
  Effectively Understand and Leverage YANG with NETCONF and
  RESTCONF for Model Drive Programmablity

Demo: Model Driven Programmability in Action
Authors: Hank Preston <hapresto@cisco.com>
         Bryan Byrne <brybyrne@cisco.com>

pull_configs.py
Illustrate the following concepts:
- Retrieve the full device configuration represented in
  YANG data models on the devices.
- Write the configurations out to files
"""

__author__ = ("Hank Preston", "Byran Byrne")
__author_email__ = ("hapresto@cisco.com", "brybyrne@cisco.com")
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import yaml
from ncclient import manager
import sys
import xml.dom.minidom

# Load Network Config Details from YAML Config File
print("Loading Network Configuration Details from YAML")
with open("config_details.yaml") as f:
    config = yaml.load(f.read())

print("Pulling network configuration from devices.")
for device in config["devices"]:
    print("  Device: {}".format(device["name"]))
    with manager.connect(host=config["network_mgmt_host"],
                         port=device["netconf_port"],
                         username=config["username"],
                         password=config["password"],
                         hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False,
                         look_for_keys=False) as m:

        netconf_reply = m.get_config('running')

        with open("device_config_backups/{}_config.xml".format(device["name"]), "w") as f:
            f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
