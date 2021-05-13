#!/usr/bin/env python3

import subprocess as sp

def pipe(p):
    scm = p.split("|")
    seg1 = scm[0].split(" ")
    seg1.remove("")
    seg2 = scm[1].split(" ")
    seg2.remove("")
    
    ps = sp.Popen(seg1, stdout=sp.PIPE).communicate()
    output = sp.Popen(seg2, stdin=ps.stdout)
    sp.wait()

def command(cm):
    #try:
        if "|" in cm:
            pipe(cm)
        else:
            seg = cm.split(" ")
            if "" in seg:
                seg.remove("")
            sp.run(seg)
    #except Exception:
    #    print("Error! Try again.")

while 1:
    ip = input("Shell >> ")
    if ip == "close":
        break
    else: 
        command(ip)
