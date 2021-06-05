#Internal Files
from Utils import *
from Characters import *

HPTXT = text(None,"green",(13,16,30),"bold",0)
MPTXT = text(None,"cyan",(13,16,30),"bold",0)

DMGTXT = text(None,"red",(13,16,30),"bold",0)

spell1 = None
spell2 = None
spell3 = None
spell4 = None

localSpells = [spell1,spell2,spell3,spell4]

class combat:
  def __init__(self,Rival):

    self.Rival = Rival

  def getRivalCast(self):
    #For now, just randomise through the Rival's spellList,
    #it isn't the best option, but it works and I don't have to do AI Stuff for it
    
    
    if Player.HP <= 0:
      if gameover() == "Retry":
        combat(Rival).main()


  def main(self):
    os.system("clear")
    #Printing out Names & Health/Mana Values

    #This could be aligned a bit better for uniformity despite naming convention, but it's a good start
    TXT.out(("Family: " + Player.family).center(30)) 
    TXT.out(("Family: " + self.Rival.family).center(30))
    TXT.out("\n",)
    TXT.out(("Name: " + Player.name).center(30))
    TXT.out(("Name: " + self.Rival.name).center(31)) 
    TXT.out("\n",)
    #add if statements so this lines up should the value reach higher digits. Maybe
    HPTXT.out(("HP:" + str(Player.HP)).center(30))
    HPTXT.out(("HP:" + str(self.Rival.HP)).center(31))

    TXT.out("\n",)

    MPTXT.out(("MP:" + str(Player.MP)).center(30)) 
    MPTXT.out(("MP:" + str(self.Rival.MP)).center(31)) 

    TXT.out("\n",)

    elementTXTs[Player.element].out(("Element:" + str(Player.element)).center(30))
    elementTXTs[self.Rival.element].out(("Element:" + str(self.Rival.element)).center(31)) 

    TXT.out("\n",)
    TXT.out("\n",)
    TXT.out("\n",)

    #Spell assigning.
    y = 0
    for x in Player.spells:

      localSpells[y] = x

      y += 1


    #Showing the player available spells
    itter = 0
    for x in localSpells:
      if x != None:
        elementTXTs[x.element].out("(" + str(itter + 1) + ") ")
        localSpells[itter].print()

        print()

        itter += 1

        #If the Player doesn't have 4 spells, I wanted to do this dynamically,
        #but JESUS CHRIST, this has taken a day and I'm not wasting more time on it. 

        #(•_•)
      elif x == None and itter < 4:
        elementTXTs[Player.element].out("(" + str(itter + 1) + ") " + "Empty Slot")
        print()      

        itter += 1

        elementTXTs[Player.element].out("(" + str(itter + 1) + ") " + "Rest")
        print()

        elementTXTs[Player.element].out("(" + str(itter + 2) + ") " + "Items")
        print()

        elementTXTs[Player.element].out("(" + str(itter + 3) + ") " + "Profile")
        print()
        print()

    #Casting
    spellsLength = (len(localSpells) - 1)
    try:
      castChoice = (int(getch()) - 1)

      if castChoice < spellsLength:
        for x in localSpells:
          if castChoice == localSpells.index(x):
            TXT.out("Who would you like to cast at?")
              
            print()

            castTarget = TXT.choice(1,self.Rival.name,"Self")

            if castTarget == 1:
              x.cast(Player,self.Rival)
              sleep(2)

            elif castTarget == 2:
              x.cast(Player,Player)          
              sleep(2)
      else:
        if castChoice == 4:
          #REST
          print("RESTING")
          sleep(2)
        if (castChoice + 1) == 5:
          Player.showitems()
          sleep(2)
        if (castChoice + 1) == 6:
          Rival.profile()
          pass 

    except:
      print((len(localSpells)))
      print(castChoice)
      print()
      TXT.out("Incorrect Value recieved, please select of the offered choices.")
          
      sleep(1)


    self.main()



  ###SCRAPYARD OF OLD IDEAS###
  
  #splChoice = TXT.choice(1, (str(localSpells[0].print()),str(localSpells[1].print()),str(localSpells[2].print()), str(localSpells[3].print())))
  
  #TXT.choice(3,localSpells[0].name + DMGTXT.out(str(localSpells[0].damage)))

  #I'm gonna be honest, I think about half of those parenthesis are necessary.

  def finalFight(self):
    pass


