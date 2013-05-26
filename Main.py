#! /usr/bin/python
# --Filename: main.py--
# brings the parts of the game togeather 


import Map
import Creatures
import time

FILE_VERSION = "0.2"
GAME_VERSION = "0.2"


def fight(monster, player):
        while True:
            if player.hp > 0:
                print "%s attacks the %s and makes %r damage!" % (player.name, monster.name, player.damage())
                monster.hp -= player.damage()
                time.sleep(1)
            else:
                print "Your Hp are 0, you died."
                # add a death function here
                break
                
            if monster.hp > 0:
                print "The %s attacks %s and makes %r damage!" % (monster.name, player.name, monster.damage())
                player.hp -= monster.damage()
                time.sleep(1)
                player.status_information()
            else:
                print "You killt the %s, now you can enter the next room!"  % monster.name
                time.sleep(3)
                break


def main():
    print "Welcome in Drageon-Cave, a little text adventure!"
    print "This is the version %s of the game :)\n" % GAME_VERSION
    print "How do you want the call your Hero?"
    player_name = raw_input("> ")
    print "Now the game can start! I hope you have fun! \n\n"
    time.sleep(3)
    player = Creatures.Player(100, player_name, 10, 1)
    
    game_map = Map.Map()
    game_map.start_game(player)



if __name__ == "__main__":
    main()
