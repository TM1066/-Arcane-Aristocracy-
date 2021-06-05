#Internal Files
from Utils import *
from Characters import *

#Class for the Spells in the game
class Spell:
  def __init__(self,name,element,manacost,damage,level):
    self.name = name
    self.element = element
    self.manacost = manacost
    self.damage = damage
    #self.effect = effect - Doing this later, just get 'em Down first

  def add(self,Char):
    Char.spells.append(self)

  def cast(self,Caster,Recipient):
    os.system("clear")

    #Successful Cast
    if Caster.MP >= self.manacost:
      Caster.MP -= self.manacost

      if self.damage >= 0:
        Recipient.HP -= self.damage
        elementTXTs[self.element].out(Recipient.name + " took " + str(self.damage) + " Points of Damage!")

      elif self.damage < 0:
        Recipient.HP += -self.damage
        elementTXTs[self.element].out(Recipient.name + " was healed for " + str(-self.damage) + " Points of Damage!")

    #Failed Cast
    elif Caster.MP < self.manacost:
      TXT.out("You don't have enough Mana!")
      





    #if Recipient.attitude = ???peaved???, etc:
      #RecipientTXT.out("MY GUY I AM SOOOAKED.")
    #Ya get it.
    #Could roll this feature into elemental stuff, so, for example, water spells do get reaction related to water and fire about being singed or something without having to write a new reaction for each spell. Help to speed up development. Intensity levels? Like, a spell could have an intensity level of between 1:3 and then I could just write 3 reactions for each attitute at each level per element? Maybe.
    pass

  def print(self):

    elementTXTs[self.element].out(self.name + ", Damage: " + str(self.damage))



#Test Spells

#FIRE
Fireball = Spell("Fireball","Fire",1,3,1)
#WATER
Waterball = Spell("Waterball","Water",1,3,1)
#NATURE
Heal = Spell("Heal","Nature",2,-3,1)
#ELECTRIC
Shock = Spell("Shock","Electric",1,3,1)


def updateEffects(Caster,Rival):
  pass