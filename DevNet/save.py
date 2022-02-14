# Exploring IOS XE YANG Data Models with NETCONF Lab

from ncclient import manager, xml_

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

# Rather than creating a NETCONF <filter> or <config>, this time we are explicitly calling the RPC from a model.
save_body = """
 <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
 """
 
# As we are sending a custom RPC, we use the dispatch method to send the custom operation.
netconf_reply = m.dispatch(xml_.to_ele(save_body))

print(netconf_reply)