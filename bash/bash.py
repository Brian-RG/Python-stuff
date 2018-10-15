import subprocess
while(1):
    a=input("Insert command: ")
    if(a=="exit"):
        break
    try:
        a=subprocess.check_output(a,shell=True)
        print(("").join(list(a.decode())))
    except:
        print("No such command")