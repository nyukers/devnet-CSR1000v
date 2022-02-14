# Cisco CSR1000v VirtualBox OVA
#
# DevOps-MDP-01, 2022

from netmiko import ConnectHandler

sshCLI = ConnectHandler(
    device_type='cisco_ios',
    host='192.168.1.19',
    port=22,
    username='admin',
    password='master'
)

print("Sending 'show ip interface brief' command to the router'...")
output = sshCLI.send_command("show ip interface brief")
print(f"IP interface status and configuration BEFORE: \n{output}\n")

config_commands = [
    'int loopback 1',
    'ip address 1.1.1.1 255.255.255.0',
    'description Loopback 1']
output = sshCLI.send_config_set(config_commands)
print(f"Config output from the device: {output}")

output = sshCLI.send_command("show ip interface brief")
print(f"IP interface status and configuration AFTER: \n{output}\n")

config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description Loopback 2']
output = sshCLI.send_config_set(config_commands)
print(f"Config output from the device: {output}")

output = sshCLI.send_command("show ip interface brief")
print(f"IP interface status and configuration AFTER2: \n{output}\n")