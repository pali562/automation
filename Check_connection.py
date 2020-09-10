# Script to check the SSH connection to device and print results in color output.
# ================================================================================

# Dependence: Paramiko must be instaled as below 
# pip install paramiko

import paramiko
import time

# Current credencials
username = 'admin'
password = 'Admin@123'

# Create instance of SSHClient object
remote_conn_pre = paramiko.SSHClient()

# Automatically add untrusted hosts 
remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

#for colorful output
CRED = '\33[41m'
CEND = '\33[0m'
CGREEN = '\33[42m'

# Log collector IP Addresses must be in the following txt file, one per line
with open (r"C:\Users\gurps\automation\Pdevice.txt") as fw:
        devices = fw.read().splitlines()


for ip in devices: 
    try:
        remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
        print(CGREEN + "SSH connection established to %s" % ip + CEND)

         
        #close the connection
        remote_conn_pre.close()

    except: 
        print (CRED + "####### The host", ip ,"has failed to respond ########" + CEND)