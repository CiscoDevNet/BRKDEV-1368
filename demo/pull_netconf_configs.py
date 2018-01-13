
from ncclient import manager
import sys
import xml.dom.minidom

# HOST = '127.0.0.1'
# HOST = 'cl-vagrant1.cisco.com'
HOST = 'cl-vagrant2.cisco.com'
USER = 'vagrant'
PASS = 'vagrant'

devices = [
    {"name": "iosxe1", "port": 2123},
    {"name": "iosxe2", "port": 2223},
    {"name": "iosxe3", "port": 2323},
    {"name": "iosxe4", "port": 2423},
]

for device in devices:
    with manager.connect(host=HOST, port=device["port"], username=USER,
                        password=PASS, hostkey_verify=False,
                        device_params={'name': 'default'},
                        allow_agent=False, look_for_keys=False) as m:

        netconf_reply = m.get_config('running')

        with open("device_config_backups/{}_config.xml".format(device["name"]), "w") as f:
            f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
