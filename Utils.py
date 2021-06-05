#Libraries
import random
import json
import sys
import os
from colr import color# <-- This is a really cool library, look into it later.
import cursor #to hide console cursor
from time import sleep
#Not working very well. Still, best way I've found ¯\_(ツ)_/¯
from getch import getch

#SETUP#
#Inital Text Speed
text_speed = 0
#Hiding Console Cursor
cursor.hide()
#Background Color
BG = (13,16,30)
lightBG = (178, 181, 194) #Tweak away

#Defining Colors
colors = {
"white" : (255,255,255),
"black" : (13,16,30),
"red" : (255,0,0),
"orange" : (255, 153, 102),
"yellow" : (255, 255, 153),
"green" : (0,255,0),
"blue" : (0, 0, 255),
"indigo" : (204, 0, 204)
}

Hcolors = {
  "Grey" : {
    "Color" : (192,192,192),
    "BGColor" : BG
  },
  "Light Blonde" : {
    "Color" : (255, 241, 133),
    "BGColor" : BG
  },
  "Blonde" : {
    "Color" : (255,215,0),
    "BGColor" : BG
  },
  "Dark Blonde" : {
    "Color" : (200, 150, 0),
    "BGColor" : BG
  },
  "Light Brown" : {
    "Color" : (205,140,70),
    "BGColor" : BG
  },
  "Brown" : {
    "Color" : (100, 75, 0),
    "BGColor" : lightBG
  },
  "Dark Brown" : {
    "Color" : (60, 30, 0),
    "BGColor" : lightBG
  },
  "Black" : {
    "Color" : (0,0,0),
    "BGColor" : lightBG
  }
}

Icolors = {
  
}

#Text Stuff

class text:
  def __init__(self,name,fcolor,bcolor,style,speed):
    self.name = name
    self.fcolor = fcolor
    self.bcolor = bcolor
    self.style = style
    self.speed = speed

  def out(self,content):
    if self.style == None and self.name == None:
      for x in color(str(content),self.fcolor,self.bcolor):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(self.speed)

    elif self.style != None and self.name == None:
      for x in color(str(content),self.fcolor,self.bcolor,self.style):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(self.speed)

    elif self.style != None and self.name != None:
      for x in color(str(self.name) + ": " + str(content),self.fcolor,self.bcolor,self.style):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(self.speed)
        
    elif self.style == None and self.name != None:
      for x in color(str(self.name) + ": " + str(content),self.fcolor,self.bcolor):
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(self.speed)               

  def choice(self,startNum,*args):
    options = []
    for y in range(startNum):
      options.append(None)
    for x in args:
      if x != None:
        options.append([str(x)])
    for x,res in enumerate(options,0):
      if res != None:
        for x in str("(" + str(x) + ")" + " " + color(res,self.fcolor,self.bcolor,self.style)):
          sys.stdout.write(x)
          sys.stdout.flush()
          sleep(self.speed)
        for x in str(len(options)):
          print("")

    return int(getch())

#Basic Text Object
TXT = text(None,(255,255,255),BG,None,text_speed)
#Player Test Text - Define in Characters.py
#PlayerTXT = text(Player.name,(255,255,255),(13,16,30),None,text_speed)
#Rival Test Text
PeaveTXT = text("Peave",(255,255,255),BG,None,text_speed)
#ASCII Art Text
ARTXT = text(None,(255,255,255),BG,"Bold",text_speed)


#Testing Hair Colors
def showHColors():
  itter = 0
  for key in Hcolors:
    HcolorTXT = text(("(" + str(itter + 1) + ") " + key),Hcolors[key]["BGColor"],Hcolors[key]["Color"],None,text_speed)


    itter += 1
    
    HcolorTXT.out(key)
    print()

def colorTests():
  choice = TXT.choice(1,"Hcolors","Icolors")
  
  print()
  if choice == 1:
    showHColors()
    getch()
    game()
#Elemental Text Stuff
ashTXT = text(None,(64, 64, 64),lightBG,"bold",text_speed)
fireTXT = text(None,(255, 107, 107),BG,"bold",text_speed)
waterTXT = text(None,(52, 235, 232),BG,"bold",text_speed)
natureTXT = text(None,(79, 255, 120),BG,"bold",text_speed)
electricTXT = text(None,(250, 255, 107),BG,"bold",text_speed)
physTXT = text(None,(133, 133, 133),BG,None,text_speed)

elementTXTs = {
  None : TXT,
  "Fire" : fireTXT,
  "Water" : waterTXT,
  "Nature" : natureTXT,
  "Electric" : electricTXT
}

#Use os library for save checking