# Exploring IOS XE YANG Data Models with NETCONF Lab

from ncclient import manager
import xmltodict
import xml.dom.minidom

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
</filter>"""

#The with statement in Python creates a context handler to automatically close resources when no longer needed. It is often used when accessing files, but can be used for other connections, like with NETCONF connections.
m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

netconf_reply = m.get_config(source='running', filter=netconf_filter)

#After the connection netconf_reply represents the rpc-reply from the device. In this line we print out the raw XML in a "pretty" fashion.
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#In these lines we convert the XML string that was returned to a Python Ordered Dictionary that can be easily manipulated, and then drill into the returned data to get a list of interfaces.
#Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]

#And finally, we loop over the interfaces, printing out the interface names and status.
for interface in interfaces:
     print("Interface {} enabled status is {}".format(
             interface["name"],
             interface["enabled"]
             )
         )