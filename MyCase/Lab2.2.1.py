# Cisco CSR1000v VirtualBox OVA
#
# DevOps-MDP-01, 2022

from netmiko import ConnectHandler

router_1 = {
    'device_type' : 'cisco_ios',
    'host' : '192.168.1.19',
    'port' : '22',
    'username' : 'admin',
    'password' : 'master',
	'secret' : 'class'
}

sshCLI = ConnectHandler(**router_1)
sshCLI.enable()

print("Sending 'show ip interface brief' command to the router'...")
output = sshCLI.send_command("show ip interface brief")
print(f"IP interface status and configuration BEFORE: \n{output}\n")

config_commands_1 = [
    'int loopback 1',
    'ip address 3.3.3.3 255.255.255.0',
    'description Loopback 1']
output = sshCLI.send_config_set(config_commands_1)
print(f"Config output from the device: {output}")

output = sshCLI.send_command("show ip interface brief")
print(f"IP interface status and configuration AFTER: \n{output}\n")