import sys
import os
from paramiko import SSHClient

print ('Target Adress:',  str(sys.argv))

server = sys.argv[0]
username = sys.argv[1]
password = sys.argv[2]
cmd_to_execute =  sys.argv[3]


ssh = SSHClient()
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
print(ssh_stdout)

