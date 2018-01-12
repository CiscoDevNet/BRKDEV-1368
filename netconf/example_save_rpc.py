from ncclient import manager, xml_
from device_info import *

save_body = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'

with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                     username=ios_xe1["username"],
                     password=ios_xe1["password"],
                     hostkey_verify=False) as m:
                     
    save_rpc = m.dispatch(xml_.to_ele(save_body))
    print(save_rpc)
    
    