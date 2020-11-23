from Game import Game

game = Game()

while not game.over:
    game.NextTurn()
    print(game.GetState())

print("Game Finished!")
