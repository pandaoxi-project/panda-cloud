from easygui import *
from re import compile

comp = r"^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$"
title = "Panda Cloud"

l = []
l = multenterbox(
    "Enter the IP you need to generate (not necessarily accessible).\n",
    title,
    ["IP: ", "Port: "],
)

if not compile(l[0]):
    msgbox("Invalid IP.", title)

with open("url", "w", encoding="utf-8") as f:
    f.write("http://%s:%s/" % (l[0], l[1]))

msgbox("Generation completed.", title)
