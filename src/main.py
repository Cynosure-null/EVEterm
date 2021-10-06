#!usr/bin/env
import os
import webbrowser
import time
from mods import *
import mods
import random
from auth import *
import json
import calls
from config import *


def zzz(seconds):
    time.sleep(seconds)

#put history files here if I screw up the echo ShIn > historyswp.txt manuver
#I forgot it's three lines. Not bloat
def HistoryADD():
    STRhistory = "echo {} >> .EVEterm/history"
    STRhistory = STRhistory.format(ShIn)
    os.system(STRhistory)

print("loading files...")



ShEx = False
devmode = False
ListHistory = False
ShIn = None
#Variable definitions
ShWelcome = "EVE-Term >"
HelpTxt = """Syntax: [COMMAND] 
Command options: 
help, man, ?: Displays this menu
server, svr: Shows server info
"""
#Removed null=None because it was useless
cnf = """
Command "{}" not found
Syntax: [COMMAND] 
Command options: 
help,: Displays this menu
server: Shows server info
WhoIs: Find the character ID for a player
ping: ping the server
sh: do a shell command
exit, esc, quit: exit the program
zkb: shows the killboard for a character id
auth: [IN PROGRESS] authenticate account
dev: allow usage of experimental commands"""
VARhistoryHELP = """
history -e-d-l-c-I
-e: enable history
-d: disable history
-l: list history
-I: Initialize history
-c: clear history
"""
ConfigHelp = '''
config -i -a -rm -l
-i initialize config
-a add line
-rm remove line
-l show config file'''

#advertising bloat
randint = random.randint(1,3)
randint = str(randint)

sponsors = "To support this project, send ISK to Misha Svargeck! And get your name mentioned in this message (if you " \
           "want that is) "
if randint =="2":
    print(sponsors)

#Config loading


while True:
    ShIn = None
    ShIn = input(ShWelcome)

    if ListHistory == True and devmode == True:
        HistoryADD()

    if ShIn == "help":
        print(HelpTxt)

    elif ShIn == "server":
        ut = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
        print(ut.text)

    elif ShIn == "WhoIs":
        mods.WhoIs()

    elif ShIn == "ping":
        mods.ping()

    elif ShIn == "zkb":
        mods.zkb()

    elif ShIn == "sh":
        mods.sh()

    elif ShIn == "dev":
        devmode = True
        print("Developer mode enabled,"
            "try unstable features at your own risk")
        ShWelcome = "EVE-Term >>"

#history
#still a work in progress

    elif ShIn == "history":
        print(VARhistoryHELP)

    elif ShIn == "history -e" and devmode == True:
        ListHistory = True
    elif ShIn == "history -I" and devmode == True:
        mods.HistInit()
    elif ShIn == "history -l" and devmode == True:
        historyLIST()
    elif ShIn == "history -c" and devmode == True:
        os.system("echo [START] > ~/.EVEterm/history")
    elif ShIn == "history -d" and devmode == True:
        ListHistory = False

    elif ShIn == "^[[A" and devmode == True:
        os.system("cat ~/.EVEterm/history | awk'END{print}'")

#config options
#still a work in progress

    elif ShIn == "config" and devmode == True:
        print(ConfigHelp)
    elif ShIn == "config -i" and devmode == True:
        #placeholder
        dummy = 1
    elif ShIn == "config -a" and devmode == True:
        ConfigAddIn = input("what would you like to run on startup?")
        ConfigAddCmd = "echo {} >> config.py"
        ConfigAddCmd = ConfigAddCmd.format(ConfigAddIn)
        os.system(ConfigAddCmd)
    elif ShIn == "config -l" and devmode == True:
        os.system("cat config.py")

    #AUTH FLOW
    #DANGER: UNSTABLE

    elif ShIn == "auth":
        if devmode == True:
            calls.auth()

#Exit loops
    elif ShIn == "esc":
        break
    elif ShIn == "exit":
        break
    elif ShIn == "quit":
        break
    elif ShIn == None:
        mods.null()

    elif ShIn == "":
        mods.null()

    elif ShIn == "" and devmode == True:
        print("Have you tried typing anything? That might solve whatever bug you are working on :) ")

    #I don't know why this is buggy. It just is. EDIT: not longer buggy!
    else:
        cnf = cnf.format(ShIn)
        print(cnf)

print("exiting shell...")
zzz(0.1)
exit()
