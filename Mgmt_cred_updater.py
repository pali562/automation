# Script to update the local password to Palo Alto Devices 
# ================================================================

# Current and new credencials must be provided
# Dependence: Paramiko must be instaled as below 
# pip install paramiko

import paramiko
import time

#For color status output about connection status
CRED = '\33[41m'
CEND = '\33[0m'
CGREEN = '\33[42m'

# Current credencials
username = input('Enter username')
password = input('Enter the current password')

# Create instance of SSHClient object
remote_conn_pre = paramiko.SSHClient()

# Automatically add untrusted hosts 
remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

# Log collector IP Addresses must be in the following txt file, one per line
with open (r"C:\Users\gurps\automation\Pdevice.txt") as fw:
        devices = fw.read().splitlines()


for ip in devices: 
    try:
        remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
        print(CGREEN + "SSH connection established to %s" % ip + CEND)

        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()

        # Strip the initial router prompt
        output = remote_conn.recv(1000)

        # Send the commands
        remote_conn.send("configure\n")
        remote_conn.send("set mgt-config user admin password\n")
        time.sleep(5)
        # New password
        npaw=input('Please enter the new password')
        remote_conn.send (npaw)
        remote_conn.send("\n")
        time.sleep(10)
        remote_conn.send(npaw)
        remote_conn.send("\n")
        time.sleep(10)
        remote_conn.send("commit\n")
        remote_conn.send("\n")
        time.sleep(15)
        remote_conn.send("exit\n")
        time.sleep(5)
        remote_conn.send("exit\n")

        # Define the buffer size
        output = remote_conn.recv(5000)

        # Print the output, with the correct tabulation	
        print(output.decode('utf-8'))
  
        #close the connection
        remote_conn_pre.close()

    except: 
        print (CRED + "####### The host", ip ,"has failed to respond ########" + CEND)