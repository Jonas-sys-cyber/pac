import os
import sys

print("Welcome to pac")
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

except:
    pass