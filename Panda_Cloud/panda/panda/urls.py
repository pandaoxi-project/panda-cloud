# This is Panda Cloud internal code. Don't modify it.
# Copyright 2022 by PanDaoxi.All rights reserved.
from django.shortcuts import HttpResponse
from django.urls import path
from json import dumps
from base64 import b64encode, b64decode ,a85encode ,a85decode
from os import walk, mkdir
from os.path import exists, join
from colorama import *
from hashlib import md5
from random import randint

# The encryption algorithm made by the author.
marks = {}
string = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~@#$%^&*()_+{}|\/{}[]<>?:;"\'=+-.,!'

# Generate character mapping dictionary
for i in range(0,len(string)):
    if i <= 9:
        marks['0' + str(i)] = string[i]
    else:
        marks[str(i)] = string[i]

# Encryption algorithm program - the first generation of DX algorithm.
class __Daoxi():
    def __init__(self):
        self.content = 'Daoxi Encode'.encode()
        self.interval_mark = '-'
        self.ec = 'UTF-8'
        self.marks = marks
    # Encryption program.
    def encode(self):
        try:
            text = a85encode(self.content).decode(self.ec)
            letters = []
            for i in text:
                letters.append(list(marks.keys())[list(marks.values()).index(i)])
            return ['OKAY',self.interval_mark.join(letters)]
        except Exception as e:
            return ['ERROR',e]
    # Decryption program.
    def decode(self):
        try:
            text = self.content.split(self.interval_mark)
            letters = []
                
            for i in text:
                letters.append(marks[i])
            result = ''.join(letters)
            return ['OKAY',a85decode(result.encode(self.ec))]
        except Exception as e:
            return ['ERROR',e]

# Generate objects.
daoxi = __Daoxi()

# ColorAMA Console palette
init()


class Colors:
    def __init__(self):
        pass

    def red(self, s):
        return Fore.RED + s + Fore.RESET

    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    def black(self, s):
        return Fore.BLACK

# Generate objects.
color = Colors()

# Create MD5 texts
getHash = lambda s: md5(s).hexdigest()

# Check whether the file is normal.
if not exists("files"):
    mkdir("files")
if not exists("BITURL"):
    with open("BITURL", "w", encoding="utf-8") as f:
        f.write("")

# When the user accesses IP:PORT/
def main(request):
    # Output the text
    print(color.magenta("A user visited the home page."))
    # Return the HTML code of the home page.
    return HttpResponse("<center><h1><b>PanDa Cloud</b></h1></center><hr>")


# When the user accesses IP:PORT/visitall
def visitall(request):
    filesTemp = []
    # Traverse the file directory and merge the names of each file into the list.
    for root, dirs, files in walk("files", topdown=False):
        for name in files:
            filesTemp.append(name)
    # Merge lists into strings for JSON.
    fileString = "/".join(filesTemp)
    # Output the text
    print(color.yellow("A user gets all the files."))
    return HttpResponse(
        dumps({"state": "okay", "files": b64encode(fileString.encode()).decode()})
    )


# When the user accesses IP:PORT/download
def download(request):
    # Set the file path to judge whether the file you want to download exists.
    want = "files\\" + request.GET.get("file")
    data = {"state": "?", "file": "", "md5": ""}
    # If the file does not exist, an error message is returned.
    if not exists(want):
        data["state"] = "THE FILE NOT FOUND"
    else:
        # Open the file you want, perform Base64 operation, and return the encrypted file field.
        with open(want, "r", encoding="utf-8") as f:
            # Panda Cloud v1.2 Improvement: encrypted storage
            daoxi.content = f.read()
            result = daoxi.decode()
            if result[0] == "OKAY": temp = result[1]
            else: 
                print(color.cyan("Error: File Read Error. %s" % want),result[1])
                return HttpResponse(dumps({'error':'yes',}))
        # Add to dictionary send to JSON.
        data["state"] = "okay"
        data["file"] = b64encode(temp).decode("utf-8")
        data["md5"] = getHash(temp).upper()
        # Output the text
        print(color.blue("A user downloaded the file: %s" % data["md5"]))
    return HttpResponse(dumps(data))


# When the user accesses IP:PORT/upload
def upload(request):
    data = {"state": "", "name": "", "md5": ""}
    # Obtain the network request sent by the client and capture the file uploaded by the user.
    want = request.POST.get("name")
    fileText = request.POST.get("text")
    with open("files/%s" % want, "w", encoding="utf-8") as f:
        # Panda Cloud v1.2 Improvement: encrypted storage.
        daoxi.content = b64decode(fileText.encode())
        text = daoxi.encode()[1]
        md5Text = getHash(text.encode()).upper()
        f.write(text)
    # Output information: a file is uploaded here.
    print(color.red("The user uploaded a file: %s" % md5Text))
    # Return request.
    data["state"] = "okay"
    data["name"] = want
    data["md5"] = md5Text
    return HttpResponse(dumps(data))


# When the user accesses IP:PORT/biturl
def biturl(request):
    want = request.GET.get("url")
    # Randomly generate a 6-character string.
    temp = []
    for i in range(0, 6):
        temp.append(
            chr([randint(65, 90), randint(97, 122)][randint(0, 1)])
        )
    tempS = "".join(temp)
    # Write short URL.
    biturl = "%s\n" % tempS
    with open("BITURL", "a", encoding="utf-8") as f:
        f.write("%s <=> %s" % (want, biturl))
    print(color.magenta("A user generated a short URL, numbered %s" % tempS))
    return HttpResponse(
        dumps(
            {
                "text": "okay",
                "biturl": "readurl?url=%s" % tempS,
            }
        )
    )


# When the user accesses IP:PORT/readurl
def readurl(request):
    # Read URL.
    with open("BITURL", "r", encoding="utf-8") as f:
        a = f.read()
    b = a.splitlines()
    c = {}
    d = ""
    e = []
    for i in b:
        d = i
        e = d.split(" <=> ")
        c[e[1]] = e[0]
    want = request.GET.get("url")
    # Open URL.
    if want in c.keys():
        print(color.magenta("A user visited a short web address, numbered %s" % want))
        return HttpResponse(' <meta http-equiv="refresh" content="0;url=%s">' % c[want])
    else:
        return HttpResponse("<h1><b>Invalid link.</b></h1>")


# Url Patterns
urlpatterns = [
    path("", main),
    path("visitall", visitall),
    path("download", download),
    path("upload", upload),
    path("biturl", biturl),
    path("readurl", readurl),
]
