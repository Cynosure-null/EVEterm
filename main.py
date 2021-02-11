#!usr/bin/env
import requests
import os
import webbrowser
import time
def zzz(seconds):
    time.sleep(seconds)

print("loading files...")

zzz(2.5)

print("Please Authenticate")
webbrowser.open('https://login.eveonline.com/oauth/authorize?response_type=code&redirect_uri=https://github.com/Changeme-NUL/EVEterm/wiki/Post-authentication&client_id=a2c6fb5fa9a3400b81eef46ea8b9c980&scope=esi-skills.read_skillqueue.v1')

ut = requests.get('https://esi.evetech.net/latest/status/?datasource=tranquility')

MUut = input("would you like to know the server info? [y/n]")

if MUut == "y":
    print(ut.content)


cid = input("enter your charecter ID here. open the link for help. https://github.com/Changeme-NUL/EVEterm/wiki/Finding-your-character-ID")

#skillquelink = ('https://esi.evetech.net/latest/characters/%/skillqueue/?datasource=tranquility' %cid)

#uname = input("enter your username here")
#pwd = input("Enter your password here. [This program does not share data with anything expect the EVE API, your data is safe]")

#cidline = "34"
print("Slight problem, this program was written by a monkey on a typewriter and you will need to edit it manualy to get it to work")
time.sleep(0.3)
instructionforediting = ("main.py line 34 replace cid with your character id")

#instructionforediting = instructionforediting.replace( fuckpython, "34")
print("lemmie just open it for you")
print("or not, coming in a later version.")



skillqueLINK = '''https://esi.evetech.net/latest/characters/12634188247/skillqueue/?datasource=tranquility'''
#skillqueLINK = skillqueLINK.format(cid)

skillquelinkREQ = requests.get(skillqueLINK)

#
# skillque = requests.get(skillquelink)

print(skillquelinkREQ.content)


wallet = requests.get('https://esi.evetech.net/latest/characters/12634188247/wallet/?datasource=tranquility' )
print(wallet)
