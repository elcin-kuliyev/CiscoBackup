import paramiko
import datetime
user = '...'
secret = '...'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
