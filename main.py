#!usr/bin/env
import requests
import os
import webbrowser
import time
from mods import *
import mods
def zzz(seconds):
    time.sleep(seconds)

print("loading files...")



ShEx = False

#Variable definitions
ShWelcome = "EVE-Term >"
HelpTxt = """Syntax: [COMMAND] 
Command options: 
help, man, ?: Displays this menu
server, svr: Shows server info
"""
null = None
cnf = """
Command "{}" not found
Syntax: [COMMAND] 
Command options: 
help,: Displays this menu
server: Shows server info"""



while ShEx == False:
    ShIn = None
    ShIn = input(ShWelcome)
    if ShIn == "help":
        print(HelpTxt)
    if ShIn == "server":
        ut = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
        print(ut.text)
    if ShIn == "WhoIs":
        mods.WhoIs()
    if ShIn == "ping":
        mods.ping()
    if ShIn == "esc":
        break
    if ShIn == "exit":
        break
    if ShIn == "quit":
        break
    else:
        cnf = cnf.format(ShIn)
        print(cnf)

print("exiting shell...")
zzz(0.1)
