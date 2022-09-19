#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
import time

today = str(datetime.now().strftime('%Y-%m-%d-%H-%M'))
filename = (today + "backup-bulanan")
tftp = '192.168.70.229'
# Device data
# Replace IP below with your ASA IP address
cisco_ios = {
    'device_type':'cisco_ios',
    'host':'172.23.2.29',
    'username':'cisco',
    'password':'cisco',
    'port':22,
    'secret':'cisco'
}

copy_cmd = "copy running-config tftp:"


net_connect = ConnectHandler(**cisco_ios)
net_connect.enable()
time.sleep(1)

output = net_connect.send_command_timing(copy_cmd)
if 'Source filename' in output:
    output += net_connect.send_command_timing('\n')
if 'remote host' in output:
    output += net_connect.send_command_timing(tftp)
if 'Destination filename' in output: 
    output += net_connect.send_command_timing(filename)
print (output)