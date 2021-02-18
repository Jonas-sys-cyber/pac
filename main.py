import os
import sys


args = []
def install(filename=str, commandname=str):
    os.system(f"chmod +x {filename}")
    os.system(f"sudo mv {filename} /usr/local/bin/{commandname}")
    print(f"sudo mv {filename} usr/local/bin/{commandname}")

for i, arg in enumerate(sys.argv):
    args.append(arg)




try:
    if args[1] == "-p" or args[1] == "--python":
        f = open("exec.sh", "a")
        f.write("#!/bin/bash \n")
        f.write(f"python3 /usr/local/bin/{args[2]}")
        f.close()
        install("exec.sh", args[3])
        os.system(f"sudo mv {args[2]} /usr/local/bin/{args[2]}")

    if args[1] == "-b" or args[1] == "--bash":
        install(args[2], args[3])

    if args[1] == "-bi" or args[1] == "--bash-install":
        assudo = input("do you want to run as root")
        if assudo == "yes" or assudo == "y":
            os.system(f"sudo sh ./{args[2]}")
        elif assudo == "no" or assudo == "n":
            os.system(f"sh ./{args[2]}")
    if args[1] == "-h":
        print("type anything and hope it works")
    if args[1] == "-g":
        os.system(f"git clone {args[2]}")
        liste = str(args[2])
        liste = liste.split("/")
        #os.system(f"cd {liste[len(liste)-1]}")
        f = open("exec.sh", "a")
        f.write("#!/bin/bash \n")
        f.write(f"python3 /usr/local/bin/{liste[len(liste)-1]}.py")
        f.close()
        install("exec.sh", args[3])
        os.system(f"sudo mv {liste[len(liste)-1]}/main.py /usr/local/bin/{liste[len(liste)-1]}.py")
        print("type yes")
        os.system(f"rm -r {liste[len(liste)-1]}")
    if args[1] == "-m" or args[1] == "--mirror":
        os.system("git clone https://github.com/luis-07/pac-mirrorlist.git")


except:
    print("typa pac -h for help")
