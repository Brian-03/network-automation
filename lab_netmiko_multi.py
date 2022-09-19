from netmiko import ConnectHandler

#create data router 
list_router=[
    {
    'device_type':'cisco_ios',
    'host':'192.168.99.1',
    'username':'cisco',
    'password':'cisco',
    'port':22,
    'secret':'cisco'
    },

    {
    'device_type':'cisco_ios',
    'host':'192.168.99.2',
    'username':'cisco',
    'password':'cisco',
    'port':22,
    'secret':'cisco'   
    },

    {
    'device_type':'cisco_ios',
    'host':'192.168.99.3',
    'username':'cisco',
    'password':'cisco',
    'port':22,
    'secret':'cisco'   
    }

]

#Global Config Mode
list_config=['int lo99',
            'description create by netmiko',
            'ip add 9.9.9.9 255.255.255.255',
            'do show ip int brief']            

for router in list_router:
    net_connect=ConnectHandler(**router)
    net_connect.enable()
    output=net_connect.send_config_set(list_config)
    print(output)



