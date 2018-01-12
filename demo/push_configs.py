
import yaml
from jinja2 import Template
from ncclient import manager
import xmltodict

# Load Configs
print("Loading Network Configuration Details from YAML")
with open("config_details.yaml") as f:
    config = yaml.load(f.read())

# Create templates
print("Setting Up NETCONF Templates")
with open("layer3_interface_config.j2") as f:
    l3_template = Template(f.read())

with open("ospf_config.j2") as f:
    ospf_template = Template(f.read())


# Loop over devices
print("Processing Device Configurations")
for device in config["devices"]:
    print("Device: {}".format(device["name"]))
    # Render Templates
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

        # Send configurations
        print("  Sending NETCONF Configuration edit-config operations")
        l3_reply = xmltodict.parse(m.edit_config(l3_config, target = "running").xml)
        ospf_reply = xmltodict.parse(m.edit_config(ospf_config, target = "running").xml)

        # Print Config Replies
        print("    Layer 3 Interface Config: {}".format(l3_reply["rpc-reply"].keys()[3]))
        print("    OSPF Config: {}".format(ospf_reply["rpc-reply"].keys()[3]))
        print("")
