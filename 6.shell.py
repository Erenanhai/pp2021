import subprocess as sp

def command(cm):
    try:
        ps = sp.run(cm.split(" "))
        return ps
    except Exception:
        print("Err404: code not found.")

while 1:
    ip = input("Shell >> ")
    if ip == "close":
        break
    else: command(ip)
    
