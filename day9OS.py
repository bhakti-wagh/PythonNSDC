import os
import os.path
import sys

print("Current direcotry:",os.getcwd())

filename="demo.txt"

if os.path.exists(filename):
    print("File exists")

else:
    print("file does not exist")


print("Command-line argument:",sys.argv)

