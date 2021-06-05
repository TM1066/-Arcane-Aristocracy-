#Internal Files
from Utils import *

def shop():
  pass


class Item:
  def __init__(self,name,value,type,colour):
    self.name = name
    self.value = value
    self.type = type
    self.colour = colour

  def use(self):
    pass

  def add(self,recipient):
    recipient.items.append(self)

gold_coin = Item("Gold Coin",15,"Valuable",(255,215,0))

potion = Item("Potion",25,"Usable",(255,0,255))