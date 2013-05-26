#! /usr/bin/python
# --Filename: creatures.py--
# define the classes creature, monsters and player
import random

FILE_VERSION = "0.3"

class Creature(object):
    """
    The parent class for monsters and player
    
    Attributes: hp, name, atk, level
    """
    
    def __init__(self, hp, name, atk, level = 1):
        self.hp = hp
        self.name = name
        self.atk = atk
        self.level = level
        
    def damage(self, weapon_atk = 0):
        return self.atk + (weapon_atk * 1.5) + random.randrange(0,6)
        
    
    def print_self(self):
        print self.hp
        print self.name    
        
        
class Monster(Creature):
    pass
    
class Player(Creature):
    
    def status_information(self):
        print "Name: %s \tHP: %d \tLevel: %d\n" %(self.name, self.hp, self.level)
    
    
    
    
if __name__ == "__main__":
    monster = Monster(120, "Gobblin")
    monster.print_self()
    
    player = Player(100, "Playername")
    player.print_self()     
