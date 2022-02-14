# Cisco CSR1000v workshop online
#
# DevOps-MDP-01, 2022

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter> """

#netconf_filtered_reply = m.get_config(source="running")
#print(netconf_filtered_reply)

netconf_filtered_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_filtered_reply.xml).toprettyxml())
