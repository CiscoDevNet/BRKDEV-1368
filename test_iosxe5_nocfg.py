
from ncclient import manager
import sys
import xml.dom.minidom

HOST = '127.0.0.1'
PORT = 2523
USER = 'vagrant'
PASS = 'vagrant'

m = manager.connect(host=HOST, port=PORT, username=USER,
                    password=PASS, hostkey_verify=False,
                    device_params={'name': 'default'},
                    allow_agent=False, look_for_keys=False)

netconf_reply = m.get_config('running')

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

m.close_session()

