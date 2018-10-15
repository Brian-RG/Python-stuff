import socket
import subprocess
HOST="localhost"
PORT=8081
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(2)
    client,address=s.accept()
    print("Connection from: "+str(address))
    while(1):
        try:
            command=client.recv(1024).decode("ascii")
            if(command=="exit"):
                client.send("Goodbye!".encode())
                break
            else:
                try:
                    if(command == None):
                        break
                    print("Command: "+command)
                    a=subprocess.check_output(command,shell=True)
                    b=(("").join(list(a.decode())))
                    client.send(b.encode())
                except:
                    client.send("No such command".encode())
        except(BrokenPipeError):
            print("error")
            break
            #client.send("Received.".encode())
            #print("Command: "+command)
    s.close()
        