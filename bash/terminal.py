import os

while(1):
    command=(os.popen(input("Insert a command: ")))
    if(command!="close"):
        try:
            print(command.read())
            command.close()
        except:
            print("No such command")