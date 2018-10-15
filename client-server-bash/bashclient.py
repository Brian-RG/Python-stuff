import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect(("localhost",8081))
    while(1):
        msg=input("Command to send: ->")
        sock.send(msg.encode())
        if(msg!="quit"):
            data=sock.recv(1024).decode('utf-8')
            print(data)
        else:
            print(sock.recv(1024).decode("utf-8"))
            break
    sock.close()
    
               