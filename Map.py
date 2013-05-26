#! /usr/bin/python
# --Filename: map.py--
# define the classes Map,
import Creatures
import Main
import random

FILE_VERSION = "0.2"


class Map(object):
    """
        Defines the rooms for the game
    """

    def __init__(self):
        pass
        
    def start_game(self, player):
        self.start_room(player)
        
    def start_room(self, player):
        gobblin = Creatures.Monster(50, "Gobblin", 3)
        player.status_information()
        
        print """
You are in the start room. In front of you is a small gobblin.
He don't look like he will let you go.
What you want to do? (Tipp: type in help for avalible options)
              """
        
        while True:
            user_action = raw_input("> ")
            if user_action == "fight": 
                print "Let the fight beginn!"
                Main.fight(gobblin, player)
                break
            elif user_action == "creeping":
                if random.randrange(0,2) > 0:
                    print "He noticed you. Now you have to fight!"
                    Main.fight(gobblin, player)
                    break
            else:
                print "Unkown option! Try again!"
                
        self.zentauer_room(player)
        
    def zentauer_room(self, player):
        zentauer = Creatures.Monster(70, "Zentauer", 5)
        player.status_information()
        
        print """
So you enterd the room of the zentauer. Normaly he's a nice guy.
But sometimes he just like to play football with the body of a human.
So don't make him angry!
              """
              
        while True:
            user_action = raw_input("> ")
            if user_action == "speak":
                if random.randrange(0,2) > 0:
                    print "Your lucky, he will let you pass!"
                    break
                else:
                    print "It's not your day! He want's to fight you!"
                    Main.fight(zentauer, player)
                    break
            else:
                print "Unkown option! Try again!"
        
        self.little_forest(player)
        
    def little_forest(self, player):
        print "a little forest" 
        player.status_information()
            
        
        
        

