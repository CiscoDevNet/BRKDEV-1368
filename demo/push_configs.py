#! /usr/bin/env python
"""
Cisco Live BRKDEV-1368:
  Effectively Understand and Leverage YANG with NETCONF and
  RESTCONF for Model Drive Programmablity

Demo: Model Driven Programmability in Action
Authors: Hank Preston <hapresto@cisco.com>
         Bryan Byrne <brybyrne@cisco.com>

push_configs.py
Illustrate the following concepts:
- Storing configuration details in external (YAML) file and
  loading dynamically into script
- Creating NETCONF XML Templates with Jinja
- Leveraging NETCONF and ncclient for pushing network
  configuration to devices
"""

__author__ = ("Hank Preston", "Byran Byrne")
__author_email__ = ("hapresto@cisco.com", "brybyrne@cisco.com")
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import yaml
from jinja2 import Template
from ncclient import manager
import xmltodict

# Load Network Config Details from YAML Config File
print("Loading Network Configuration Details from YAML")
with open("config_details.yaml") as f:
    config = yaml.load(f.read())

# Create Jinja Template Objects for NETCONF Payloads
print("Setting Up NETCONF Templates")
# Layer 3 Interface Configurations
with open("layer3_interface_config.j2") as f:
    l3_template = Template(f.read())

# OSPF Routing Configuration
with open("ospf_config.j2") as f:
    ospf_template = Template(f.read())


# Loop over network devices to create and deploy network config
print("Processing Device Configurations")
for device in config["devices"]:
    print("Device: {}".format(device["name"]))
    # Create Device Specific Configurations
    print("  Creating Device Specific Configurations from Templates")
    with open("netconf_configs/{}_layer3.cfg".format(device["name"]), "w") as f:
        l3_config = l3_template.render(interfaces=device["interfaces"])
        f.write(l3_config)
    with open("netconf_configs/{}_ospf.cfg".format(device["name"]), "w") as f:
        ospf_config = ospf_template.render(ospf=device["ospf"])
        f.write(ospf_config)

    # Connect to Device with NETCONF
    print("  Connecting to device with NETCONF")
    with manager.connect(host=config["network_mgmt_host"],
                         port=device["netconf_port"],
                         username=config["username"],
                         password=config["password"],
                         hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False,
                         look_for_keys=False) as m:

        # Send NETCONF Configurations with <edit-config> RPC
        print("  Sending NETCONF Configuration edit-config operations")
        l3_resp = m.edit_config(l3_config, target = "running")
        ospf_resp = m.edit_config(ospf_config, target = "running")

        # Process XML data in replies
        l3_reply = xmltodict.parse(l3_resp.xml)
        ospf_reply = xmltodict.parse(ospf_resp.xml)

        # Print Config Replies
        print("    Layer 3 Interface Config: {}".format(l3_reply["rpc-reply"].keys()[3]))
        print("    OSPF Config: {}".format(ospf_reply["rpc-reply"].keys()[3]))
        print("")
