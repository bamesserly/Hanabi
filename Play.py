from Game import Game
import sys

game = Game()

while not game.over:
    try:
        new_state = game.NextTurn()
        print(new_state)
    except AssertionError:
        print("Error: game state did not change when a turn was taken")
        sys.exit(1)

print("Game Finished!")
