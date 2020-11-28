from Game import Game
import sys

game = Game()

while not game.over:
    try:
        new_state = game.NextTurn()
    except AssertionError:
        print("Error: game state did not change when a turn was taken.")
        sys.exit(1)

print("Game finished.")
if all(i == 5 for i in game.piles.values()):
    print("Fireworks! You Win!")
else:
    print("Too bad, you lose with a score of", game.GetScore())
