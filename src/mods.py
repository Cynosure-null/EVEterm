#!usr/bin/env
import requests
import urllib.parse
import webbrowser
import time
import os

def ServerInfo():
    ut = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
    print(ut.text)

#I don't know what the hell this is supposed to do. I think it might be important though
"""
def NoAuthRequest():
    Nar_url = requests.get(lonk)
"""
def null():
    None

def sh():
    ShellInput = input("$ ")
    os.system(ShellInput)

def reset():
    ShIn = None

def WhoIs():
       WhoIsCHR = input("Who do you want to find an ID for?")
       WhoIsCHR = urllib.parse.quote(WhoIsCHR)
       WhoIsCHR = str(WhoIsCHR)
       WhoIsLINK = "https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search={}&strict=false"
       WhoIsLINK = WhoIsLINK.format(WhoIsCHR)
       WhoIsIN = requests.get(WhoIsLINK)

       WhoIsIN = WhoIsIN.text

       WhoIsRes = ("""{}
       This is your requested character ID""")
       print(WhoIsIN)
       print("This is your requested character ID")

def zkb():
    zkbin = input("enter the character ID you would like to see the killboard for")
    zkbin = str(zkbin)
    zkbin = urllib.parse.quote(zkbin)
    zkbin = str(zkbin)
    zkblink = "https://zkillboard.com/character/{}/"
    zkbout = zkblink.format(zkbin)
    webbrowser.open_new_tab(zkbout)


def ping():
    time1 = time.time()
    PingREQ = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
    time2 =time.time()
    time3 = time2-time1
    print(time3)



def HistInit():
    os.system("mkdir .EVEterm")
    os.system("echo [START] > .EVEterm/history ")

def historyADD():
    STRhistory = "echo {} >> .EVEterm/history"
    STRhistory = STRhistory.format(ShIn)
    os.system(STRhistory)

def historyLIST():
    os.system("cat .EVEterm/history")

def historyCLR():
    os.system("echo [START] > .EVEterm/history ")


