import sys
import os
import paramiko 
import time

# open credentials.txt file for reading 
with open('credentials.txt') as f:
    creds = [line.rstrip() for line in f]

# open payload.txt file for reading 
with open('payload.txt') as f:
    payload = [line.rstrip() for line in f]

# connect to host with creds in payload.txt
host = creds[0]
port = 22
username = creds[1]
password = creds[2]

# ssh connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# payload all the things 
for command in payload:
    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(1)
    lines = stdout.readlines()
    print(lines)

# ssh.close()
