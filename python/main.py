#import game.characters.player

#game.characters.player.get_player_info()




# We can also use the from import statement to import only certain modules from the package.

from game.characters import player
from game.characters.boss import get_boss_info

# here we have only imported the player module of the characters sub package so we can access the get player info function without using the game package 

player.get_player_info()

get_boss_info()