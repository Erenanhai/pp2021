import subprocess as sp

while 1:
    ip = input("Shell >> ")
    ps = sp.run(ip.split(" "))
