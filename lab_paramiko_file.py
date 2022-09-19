import paramiko
import json
import time
#open and read list device on csv file
data_router=open('data_router.csv','r').readlines()
data_router.remove(data_router[0])

#input data to list 
data_router_list=[]
error_list=[]

for router in data_router:
    router=router.split(',')
    data_router_list.append({
        "ip":router[0],
        "user":router[1],
        "passw":router[2],
        "port":router[3].strip()
    })

# print(json.dumps(data_router_list,indent=3))

#koneksi ssh to device

for router in data_router_list:
    try:
        ssh_client=paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=router["ip"],
            username=router["user"],
            password=router["passw"],
            port=router["port"]
        )

        print(f"Success Login to {router['ip']}")
        conn = ssh_client.invoke_shell()
        conn.send("show ip int brief\n")
        time.sleep(2)

        output=conn.recv(65535).decode()
        print(output)
        ssh_client.close()

    except Exception as message:
        print(message)
        error_list.append(router['ip'])
        continue


if len(error_list)>0:
    print(f"ini adalah router yg error{error_list}")






