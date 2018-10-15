import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.11",8081))
#sock.connect(("localhost",8081))
while(1):
    msg=input("Message to send: ->")
    sock.send(msg.encode())
    if(msg!="quit"):
        data=sock.recv(1024).decode('utf-8')
        print("El servidor envió: " +data)
    else:
        print(sock.recv(1024).decode("utf-8"))
        break
sock.close()

           