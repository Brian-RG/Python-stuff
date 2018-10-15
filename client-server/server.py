import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.0.11",8081)) #Using IP address
#sock.bind(("localhost", 8081)) #Using localhost. also works with loopback 127.0.0.1, Assigning the server port and host
sock.listen(2)
conn, addr = sock.accept() #returns tupple
print("Connection from: "+str(addr))
while(1):
    data= conn.recv(1024).decode("ascii") 
    if(data!="quit"):
        conn.send("Thanks for the message".encode())
        print(data)
    else:
        conn.send("Goodbye!".encode())
        break
sock.close()