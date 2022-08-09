# Use this program to open Panda Cloud.
# Copyright 2022 by PanDaoxi.All rights reserved.
# E-mail: 2060642520@qq.com
# See https://pandaoxi.blog.csdn.net/
# Date: 2022-3-20  Time: 13:05

# Import package
from os import name, system
from time import strftime
from socket import socket, AF_INET, SOCK_DGRAM

# Get LAN IP address
def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


# Create server
def main():
    ip = getIP()
    port = strftime("%Y")
    setIP = ip + ":" + port
    print("Get IP address: http://%s/\nPort number: %s (Current year)" % (ip, port))
    print("Creating server, please wait...\n\n")
    system(r"python .\panda\manage.py runserver %s" % setIP)


# Run the current program
if __name__ == "__main__" and name == "nt":
    main()
    input("")
else:
    print(
        "Your PC can't run this program because:\n(1) Non autonomous operation procedures;\n(2) You are not using a Windows operating system.\nIf it cannot be solved, please contact the developer."
    )
    input("")
