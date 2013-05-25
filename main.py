#! /usr/bin/python
# --Filename: main.py--
# brings the parts of the game togeather 


import Map
import Creatures

FILE_VERSION = "0.0.1"

def main():
    
    
    print "How do you want the call your Hero?"
    player_name = raw_input("> ")
    player = Creatures.Player(100, player_name, 10)
    
    game_map = Map.Map()
    game_map.start_game(player)



if __name__ == "__main__":
    main()
