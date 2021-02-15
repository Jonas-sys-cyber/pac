import os
import sys

args = []
for i, arg in enumerate(sys.argv):
    args.append(arg)

def install(filename=str, commandname=str):
    os.system(f"chmod +x {filename}")
    os.system(f"sudo mv {filename} /usr/local/bin/{commandname}")
    print(f"sudo mv {filename} usr/local/bin/{commandname}")


if args[1] == "-b" or args[1] == "--bash":
    install(args[2], args[3])
