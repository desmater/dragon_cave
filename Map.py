#! /usr/bin/python
# --Filename: map.py--
# define the classes Map,
import Creatures

FILE_VERSION = "0.0.1"


class Map(object):
    """
        Defines the rooms for the game
    """

    def __init__(self):
        pass
    
    def player_information(self, player):
        print "Name: %s \tHP: %d \tLevel: %d" %(player.name, player.hp, 1)
        
    def start_game(self, player):
        self.start_room(player)
        
    def start_room(self, player):
        self.player_information(player)
        print "start_room"
        gobblin = Creatures.Monster(50, "Gobblin", 3)
        while player.hp > 0 or gobblin.hp > 0:
            print "Player atk:", player.damage()
            gobblin.hp = gobblin.hp - player.damage()       # fail here pls make better ;D
            print "Enemy atk:", gobblin.damage()
            player.hp = player.hp - gobblin.damage()
        
        self.zentauer_room(player)
        
    def zentauer_room(self, player):
        self.player_information(player)
        print "zentauer_room"
        self.little_forest(player)
        
    def little_forest(self, player):
        self.player_information(player)
        print "a little forest"     
        
        
        

