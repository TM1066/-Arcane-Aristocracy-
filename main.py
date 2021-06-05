#Internal Files
from Utils import *
from Settings import *
from Combat import *
from Spells import *
from Characters import *
from Items import *
#External Libraries in Utils.py



###Defining Rivals & Subsequent Battles###

#Phyte Family - Physical Fighters
MPhyte = Character("Mordecai","Phyte","Male","Brown","Brown",20,None,1,10,0)
NPhyte = Character("Null","Phyte","Female","Grey","Brown",35,None,3,35,0)
SPhyte = Character("Sanford","Phyte","male","Light Brown","Brown",50,None,5,50,5)

PhyteFamily = [MPhyte,NPhyte,SPhyte]
#Frig Family - Water/Ice Fighters
KFrig = Character("Kriil","Frig","Male","Grey","Dark Blue",60,"Water",7,45,30)
LFrig = Character("Laor","Frig","Female","Light Blonde","Light Blue",70,"Water",9,50,45)
MFrig = Character("Maelik","Frig","Male","White","Grey",85,"Ice",11,65,65)

FrigFamily = [KFrig,LFrig,MFrig]
#Ashine Family - Fire Fighters
AAshine = Character("Alphonse","Ashine","Male","Red","Dark Blue",60,"Fire",10,50,65)
AsAshine = Character("Aster","Ashine","Male","Grey","Dark Blue",100,"Fire",15,65,50)
WAshine = Character("Walster","Ashine","Male","Black","White",0,"Ash",20,100,999)

AshineFamily = [AAshine,AsAshine,WAshine]

Families = [PhyteFamily,FrigFamily,AshineFamily]

#The actual game stuff

def inTime():
  #Inbetween Fights
  pass

def gameOver():
  art = open("ASCII/GameOver.txt","r")
  ARTXT.out(art.read() + "\n\n")
  art.close()
  print()
  print()
  TXT.out("Bad News! I haven't made saving a thing yet...")
  sleep(3)
  print()
  print()
  TXT.out("Retry Battle?")
  retry = TXT.choice(1,"YES!","no... (Restart)")

  if retry == 1:
    Player.refresh()
    Rival.refresh() #Defined with each instance of Combat
    return "retry"
  
  elif retry == 2:
    #SHOULD restart program. Emphasis on SHOULD, in case the caps went unnoticed.
    os.execl(sys.executable, sys.executable, *sys.argv)

def gameEnd():
  pass

def game():
  #Making Character & Parent
  charcreator()
  os.system("clear")

  #First Family
  for x in Families[0]:
    combat(PhyteFamily[x])
    inTime()  
  #Second Family
  for x in Families[1]:
    combat(FrigFamily[x])
    inTime()
  #Final Family
  for x in Families[2]:
    combat(AshineFamily[x])
    inTime()


def main():
  
  art = open("ASCII/MainMenu.txt","r")
  ARTXT.out(art.read() + "\n\n")
  art.close()

  choice = TXT.choice(1,"Begin","Settings","Show Items","Test Fight","Color Tests")

  if choice == 1:
    game()


  elif choice == 2:
    os.system("clear")
    化_settings()

  elif choice == 3:
    os.system("clear")
    Player.showItems()
    
  elif choice == 4:
    os.system("clear")
    debugFight = combat(Peave)
    debugFight.main()

  elif choice == 5:
    os.system("clear")
    colorTests()

  

main()
