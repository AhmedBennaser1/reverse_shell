import sys
import socket 



LHOST= "192.168.1.135"
LPORT = 4444

s= socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((LHOST,LPORT))


s.listen(1)

while True:
    print(f'[+] listening as {LHOST}:{LPORT}')

    client=s.accept()
    print(f'[+] client connected to {client[1]}')

    client[0].send('Connected'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())
        
        if cmd.lower() in ['quit' ,'ex' ,'q' , 'x' ,'exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd=input('Wait for new client y/n') or 'y'

    if cmd.lower() in ['n','no','nay']:
        break

s.close()



