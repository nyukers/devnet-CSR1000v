:curl -i -k -X "OPTIONS" "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" -H 'Accept:application/yang-data+json' -u 'developer:C1sco12345'
:curl -i -k -X "OPTIONS" "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces" -H 'Accept:application/yang-data+xml','Content-type:application/yang-data+xml' -u 'developer:C1sco12345'
                                
:curl -i -k -X "OPTIONS" "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" -H 'Accept:application/yang-data+json' -u 'developer:C1sco12345'

:pyang -f tree ietf-interfaces.yang

ssh -oHostKeyAlgorithms=+ssh-dss developer@sandbox-iosxe-latest-1.cisco.com -p 830 -s netconf