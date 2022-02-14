# Exploring IOS XE YANG Data Models with NETCONF Lab
# Create an XML configuration template for ietf-interfaces

from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

netconf_interface_template = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface operation="delete">
             <name>{name}</name>
         </interface>
     </interfaces>
</config>"""

# Next the script asks the user for the details on a new Loopback interface to add.
# Ask for the Interface Details to Add
new_loopback = {}
#new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
#new_loopback["desc"] = input("What description to use? ")

new_loopback["type"] = "loopback"
new_loopback["status"] = "true"

#new_loopback["ip_address"] = input("What IP address? ")
#new_loopback["mask"] = input("What network mask? ")

new_loopback["name"] = "Loopback99"
new_loopback["desc"] = "Loopback99"
new_loopback["ip_address"] = "100.100.100.100"
new_loopback["mask"] = "255.255.255.0"


# Here the template is combined with the data from the user.
# Create the NETCONF data payload for this interface
netconf_data = netconf_interface_template.format(
         name = new_loopback["name"],
         desc = new_loopback["desc"],
         type = new_loopback["type"],
         status = new_loopback["status"],
         ip_address = new_loopback["ip_address"],
         mask = new_loopback["mask"]
     )

# Lastly, here the <edit-config> operation is executed.
netconf_reply = m.edit_config(netconf_data, target = 'running')
