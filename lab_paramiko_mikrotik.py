import paramiko
import time
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.99.2",username="admin",password="idnmantab")

stdin, sdtout,stderr=ssh.exec_command("ip address print")
print(sdtout.read().decode("ascii")).strip("\n")
ssh.close()

