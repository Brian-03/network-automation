from netmiko import ConnectHandler

data_router=open('data_router.csv','r').readlines()
data_router.remove(data_router[0])


list_config=[#'int lo99',
            #'description create by netmiko',
            # 'ip add 9.9.9.9 255.255.255.255',
            'vlan 192',
            'name tes',
            'vlan 193',
            'name tes1',
            'vlan 195',
            'name Tesss',
            'do wr',
            'do show vlan br']

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
    output=net_connect.send_config_set(list_config)
    get_hostname = net_connect.send_command("show running-config | s hostname")

    print(output)
    #export configuration
    verif=net_connect.send_multiline(commands)
    save=open(f'GAMA_{get_hostname.split(" ")[1]}.txt','w')
    save.write(verif)
    save.close()

#user ssh privilage harus 15



