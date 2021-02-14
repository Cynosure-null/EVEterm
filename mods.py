#!usr/bin/env
import requests
import urllib.parse
import webbrowser
import time

def ServerInfo():
    ut = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
    print(ut.text)

def NoAuthRequest():
    Nar_url = requests.get(lonk)

def reset():
    ShIn = None

def WhoIs():
       WhoIsCHR = input("Who do you want to find an ID for?")
       WhoIsCHR = urllib.parse.quote(WhoIsCHR)
       WhoIsCHR = str(WhoIsCHR)
       WhoIsLINK = "https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search={}&strict=false"
       WhoIsLINK = WhoIsLINK.format(WhoIsCHR)
       WhoIsIN = requests.get(WhoIsLINK)
       WhoIsOUT = WhoIsIN.format(WhoIsCHR)
       WhoIsRes = ("""{}
       This is your requested character ID""")
       WhoIsRes = WhoIsRes.format(WhoIsOUT)
       print(WhoIsRes)

def zkb():
    zkbin = input("enter the charecter ID you would like to see the killboard for")

def ping():
    time1 = time.time()
    PingREQ = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
    time2 =time.time()
    time3 = time1-time2
    print(time3)

"""
def MishaSvargeck():
    Make.Function()
    Emotion = \"Happy \" 
    exit()
    """
