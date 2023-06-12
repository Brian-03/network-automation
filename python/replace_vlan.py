from netmiko import ConnectHandler

data_router=open('data_router.csv','r').readlines()
data_router.remove(data_router[0])


#Identify interfaces with VLAN 
interface_output = 'do show interfaces status | include _4_'


for router in data_router:
    router=router.split(',')
    router_dict={
        'device_type': 'cisco_ios'if router[4].strip()=="ssh" else "cisco_ios_telnet",
        'host':router[0],
        'username':router[1],
        'password':router[2],
        'port':router[3].strip() #if router[3].strip() else 22
    }
    #koneksi ssh ke device
    commands = []
    command_files= open('configfile.csv','r').readlines()

    for commandFile in command_files:
        commands.append(commandFile.replace('\n',""))

    net_connect=ConnectHandler(**router_dict)
    net_connect.enable()
    output=net_connect.send_config_set(interface_output)

    get_command = [line.split()[0] for line in output.split('\n') if line.strip()]
    interfaces = list(filter(lambda interface: interface.startswith('Gi'), get_command ))

    #Add the access List and other contigs to those interfaces 
    interfaces_config = []
    for interface in interfaces:
        interface_config = [
            'interface %s' % (interface),
            'switchport mode access',
            'switchport access vlan 6',
        ]

        interfaces_config.append(interface_config)

    for execute_command in interfaces_config:
        net_connect.send_config_set(execute_command)

    print('Host: %s' % (get_command[len(get_command) - 1]))
    print(net_connect.send_command('show interfaces status'))
    get_hostname = net_connect.send_command("show running-config | s hostname")

    #export configuration
    verif=net_connect.send_multiline(commands)
    save=open(f'GAMA_{get_hostname.split(" ")[1]}.txt','w')
    save.write(verif)
    save.close()

#user ssh privilage harus 15



