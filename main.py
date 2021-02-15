
import os
import sys
args = []
for i, arg in enumerate(sys.argv):
    args.append(arg)
print(args[1])
def install(directory=str,filename=str, commandname=str):
    os.system(f"chmod +x {filename}")
    os.system(f"sudo mv {filename} /usr/local/bin/{commandname}")
    print(f"sudo mv {filename} usr/local/bin/{commandname}")

#install("home/luis/Downloads/", "command.sh", "testcommand")
install("~/", "test.sh", "neo")

if args[1] == 