# Cisco CSR1000v workshop online
#
# DevOps-MDP-01, 2022

from ncclient import manager

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

print("The suported capabilities are:")
for capability in m.server_capabilities:
    if "Cisco-IOS-XE-cdp" in capability:
        print(capability)

m.close_session()