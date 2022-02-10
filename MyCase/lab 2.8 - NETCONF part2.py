from ncclient import manager
from xml.dom.minidom import *

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )
# Changing the hostname
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>NEWHOSTNAME</hostname>
    </native>
</config>"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Creating a Loopback interface
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>100</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Trying to create a new Loopback interface with the same IP address as the previous one
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>111</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

