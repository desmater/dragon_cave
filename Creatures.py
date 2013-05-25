#! /usr/bin/python
# --Filename: creatures.py--
# define the classes creature, monsters and player

FILE_VERSION = "0.0.1"

class Creature(object):
    """
    The parent class for monsters and player
    
    Attributes: hp, name
    """
    
    def __init__(self, hp, name, atk):
        self.hp = hp
        self.name = name
        self.atk = atk
        
    def damage(self, weapon_atk = 0):
        return self.atk + (weapon_atk * 1.5)
    
    def print_self(self):
        print self.hp
        print self.name    
        
        
class Monster(Creature):
    pass
    
class Player(Creature):
    pass
    
    
    
    
if __name__ == "__main__":
    monster = Monster(120, "Gobblin")
    monster.print_self()
    
    player = Player(100, "Playername")
    player.print_self()     
