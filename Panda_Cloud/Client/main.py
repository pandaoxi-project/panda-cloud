# Import package.
from requests import post, get
from tkinter import Tk
from tkinter.filedialog import *
from os import remove, environ, name, system
from os.path import exists, splitext
from time import strftime
from easygui import *
from socket import socket, AF_INET, SOCK_DGRAM
from base64 import b64encode, b64decode
from sys import exit
from re import compile
from webbrowser import open as openW

# Declare the settings of variables and packages that the program depends on.
title = "Panda Cloud (Client)"
hide = Tk()
hide.withdraw()
desktop = environ["USERPROFILE"] + "\\Desktop"

# Declare the settings of variables and packages that the program depends on.
def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


# First, use file search to obtain the server. If not, use the LAN IP of the current computer.
if exists("url"):
    with open("url", "r", encoding="utf-8") as f:
        ip = f.read()
else:
    ip = "http://%s:%s/" % (getIP(), strftime("%Y"))

# File upload function
def upload():
    upd = askopenfilename(title=title, filetypes=[("All Files", "*.*")])
    with open(upd, "rb") as f:
        temp = b64encode(f.read()).decode()
    up = upd.split("/")
    data = {
        "name": up[len(up) - 1],
        "text": temp,
    }
    res1 = post(ip + "upload", data=data).json()["state"]
    if res1 == "okay":
        msgbox("File upload succeeded.", title)


# File download function
def download():
    res1 = get(ip + "visitall").json()["files"]
    file_list = b64decode(res1.encode()).decode().split("/")
    if res1 != "":
        cho = choicebox("Please select the file to download.", title, choices=file_list)
        res2 = get(ip + "download?file=%s" % cho).json()
        fileText = b64decode(res2["file"].encode())
        types = splitext(cho)[1]
        dow = asksaveasfilename(
            title=title,
            filetypes=[("All Files", types)],
            initialfile=cho,
            initialdir=desktop,
        )
        with open(dow, "wb") as f:
            f.write(fileText)
        msgbox("File download succeeded.", title)
    else:
        msgbox("You haven't uploaded any files yet. Please upload one first.", title)

# Short URL function
def biturl():
    url = enterbox("Enter the original URL you need to generate a short URL:", title)
    comp = r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    if not compile(url):
        msgbox("The URL you entered is incorrect. Please re-enter it.", title)
        exit()
    res1 = get(
        ip + "biturl",
        params={
            "url": url,
        },
    ).json()
    if res1["text"] == "okay":
        bitu = ip + res1["biturl"]
        msgbox(
            "Your short URL was generated successfully! You can visit the following website.\n\nOriginal website: %s\nShortened URL: %s"
            % (url, bitu),
            title,
        )


# Main function (task assignment function)
def main():
    t = ["File Upload", "File Download", "Short URL", "About", "Switch Server", "Exit"]
    cho = buttonbox("Please select the service you need.\nServer: %s" % ip, title, t)
    if cho == t[0]:
        upload()
    elif cho == t[1]:
        download()
    elif cho == t[2]:
        biturl()
    elif cho == t[3]:
        textbox(
            "Here are some information about us:",
            title,
            text="About us:\nBlog: https://pandaoxi.blog.csdn.net/\nOur email: 2060642520@qq.com\nWechat: pandaoxi2021\nQQ:3377063617\n\nWelcome to this program! This program is designed to help all users in the LAN carry out network transmission, and the main functions are as follows:\n1. Server cloud storage;\n2. Upload and download files quickly (without speed limit);\n3. Shorten the website quickly to make access more convenient;\n4. The program runs quickly and supports multiple operating systems;\n5. Encrypted file transmission.\nIf you have any related questions, you can use any of the contact information mentioned above to contact us for reporting; If an error is found during the operation of the program, please report it to the developer. thank!",
        )
    elif cho == t[4]:
        if name == "nt":
            temp = get('https://pandaoxi.coding.net/p/pandaoxi/d/PanDaoxi/git/raw/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud/URL_Generation_Tool.exe')
            with open('function.exe','wb') as f:
                f.write(temp.content)
            system('call function.exe')
        else:
            openW("https://pandaoxi.coding.net/public/pandaoxi/PanDaoxi/git/files/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud/URL_Generation_Tool.py")
        msgbox("You can use this program to modify the IP address of the program.",title)
        exit()
    else:
        exit()


# Judge operating conditions
if __name__ == "__main__":
    try:
        while True:
            main()
    except Exception as e:
        msgbox(
            "A fatal error has occurred in the program, so the program cannot run. Please send this message to the developer: %s"
            % e,
            title,
        )
hide.mainloop()
