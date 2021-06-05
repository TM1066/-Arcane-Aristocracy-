#Internal Files
from Utils import *

#Class for difficulties, this is used for scaling health gain, spell damage, etc
#class difficulty:
  #def __init__(self,name,)


#Menu options
def seedSet():
    os.system("clear") #Repeating for Safety & Code loops
    TXT.out("Gimme' a Numba':")
    try:
      random.Seed = int(input())
      os.system("clear")
      TXT.out("Seed Set!")
      sleep(1)
      化_settings() #Neat! You can call a thing-y before it's defined.
    except:
      TXT.out("I said number, my guy. Try again.")
      sleep(2)
      seedSet()

def speedSet():
    os.system("clear") #Repeating for Safety & Code loops
    TXT.out("(It is recommended to stay at Instant, but far be it from me to take agency away from the Player.)\n\n")
    choice = TXT.choice("Slow","Medium","Fast","Instant")

    try:
      if choice == 1:
        text_speed = 0.1
      elif choice == 2:
        text_speed = 0.05
      elif choice == 3:
        text_speed = 0.01
      elif choice == 4:
        text_speed = 0

      TXT.speed = text_speed

      os.system("clear")
      TXT.out("Speed Set!")
      sleep(1)
      化_settings() #Neat! You can call a thing-y before it's defined.
    except:
      TXT.out("I said number, my guy. Try again.")
      sleep(2)
      seedSet()
def textChange():
  pass

def 化_settings():
  os.system("clear")
  art = open("ASCII/Settings.txt","r")
  ARTXT.out(art.read() + "\n\n")
  art.close()
  
  choice = TXT.choice("Change Difficulty","Change Player Text","Change Text Speed","Change Random Seed")
  if choice == 1:
    化_settings()
    #diffSet()
  elif choice == 2:
    化_settings()
    #textSet()
  elif choice == 3:
    speedSet()
  elif choice == 4:
    seedSet()