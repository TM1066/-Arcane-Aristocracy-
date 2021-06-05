#Internal Files
from Utils import *
from Spells import *
from Items import *
text_speed = 0.01

#Class for the Player
class Character:
  def __init__(self,name,family,gender,hcolor,icolor,Money,element,level,HP,MP):
    self.name = name
    self.family = family
    self.gender = gender
    self.hcolor = hcolor
    self.icolor = icolor
    self.element = element
    self.level = level
    self.HP = HP
    self.MP = MP
    self.InitalHP = HP
    self.InitalMP = MP
    self.spells = []
    self.items = []

  def refresh(self):
    self.HP = self.InitalHPHP
    self.MP = self.InitalMP

  def relationSet(self,F_or_M):
    #Just doing Parent stuff right now, may expand in the future, hence the method.

    if F_or_M == "F":
      self.relation = "Father"
    elif F_or_M == "M":
      self.relation = "Mother"

  #Accesible from Profile & Shop
  def showItems(self):
    itter = 0
    itemList = []
    for x in self.items:
      itemTXT = text(None,x.colour,(13,16,30),None,text_speed)

      itemTXT.out("(" + str(itter + 1) + ") " + self.items[itter].name)
      print()
      itter += 1

  def profile(self):
    #For now, I'm just displaying the profile,
    #In the future, add numbers before each print out call and check for player input leading to a description of each constituent part. I.E. a piece of text like "These are //Blue\\ Eyes, they are like, totes blue."

    TXT.out(("Given Name: " + str(self.name)).center(30))
    TXT.out(("Family Name: " + str(self.family)).center(30))
    print()
    print()
    TXT.out(("Gender: " + str(self.gender)).center(30))

    TXT.out(("Giv: " + str(self.name)).center(30))
    print()
    pass

  def lvlup(self):
    self.level += 1
    #Some math stuff, I suck at this, point is: Scale damage with level dynamically
    for x in self.Spells:
      x.damage += (self.level / 1.5) 

    #use a check accessible spell function to return whether the player has unlocked a new spell

    def checkSpell(self):
      pass
      #use self.element and keep a list of spells in a json file or something, then cross check between player level and spell level

  def random(self):
    pass
    #return random character

  #Method for creating a new character based on Parent Character
  def descend(self,secondChar):
    pass


#Placeholder Player Character
Player = Character("Sallow","Spellman","Male","Brown","Brown",0,"Fire",1,10,5)
#Testing Spell Stuff
Fireball.add(Player)
Waterball.add(Player)
Heal.add(Player)
#Shock.add(Player)
#Testing Item Stuff
gold_coin.add(Player)
potion.add(Player)


#Placeholder Rival
Peave = Character("Peave","Angery","Rage","White","Black",0,"Electric",5,25,20)


#Player creates parents and then has to pick whilst randomizing themselves - Emphasis the choice being revoked as it is in most cases, despite the player ultimately ending up pretty well off.

#This will be the intro to the game, but, for now, I'm just focusing on the main meat of the game.

def charcreator():
  os.system("clear")

  Player = Character(None,None,None,None,None,None,None,None,None,None)

  Parent = Character(None,None,None,None,None,None,None,None,None,None)

  TXT.out("Which Parent would you like to customise?\n\n") #DEFINITLY NOT THE FINAL BOSS. THAT WOULD BE SOOO UNCOOL.

  choice = TXT.choice(1,"Father","Mother")
  if choice == 1:
    Parent.gender = "Male"
    Parent.relationSet("F")
  elif choice == 2:
    Parent.gender = "Female"
    Parent.relationSet("F")

  os.system("clear")

  Parent.profile()

  TXT.out("Describe your Characters " + Parent.relation)

  choice = TXT.choice(1,"Family Name","Hair Colour","Eye Colour")

  if choice == 1:
    pass
  elif choice == 2:
    choice = TXT.choice("Premade Hair Colors","Custom Hair Color (WIP)")
    os.system("clear")
    showHColors()
    print()
    print()
    TXT.out("Please Select a Color.")
    #choice = 
  elif choice == 3:
    pass

  #Allow for the choice of premade colours or the custom input of colours 


  for value in Parent.__dict__:
    if value == None:
      TXT.out("Not all options have been defined, please fully customise your Parent.")
  

