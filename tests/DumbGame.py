import random

class Game:

    def __init__(self):
        print("New Game. Guess the correct order of numbers 0-5 with a partner. 7 strikes and you're out.")
        self.over = False
        self.n_strikes = 8
        self.numbers = list(range(0,5))
        random.shuffle(self.numbers)
        self.acting_player_index = 0
        self.score = 0
        self.state = self.GetState()

    def GetActingPlayerIndex(self):
        return self.acting_player_index

    def GetNextPlayerIndex(self):
        return (self.acting_player_index + 1) % 2

    def GetState(self, player_idx=None):
        s = []
        s.append(self.n_strikes)
        s.append(self.acting_player_index)
        s.append(self.score)
        # conceal solution from player
        if player_idx is not None:
            self.state.append("")
        else:
            s.append(self.numbers)
        return s

    def NumberIsPlayable(self, guessed_number):
        return self.numbers[self.score] == guessed_number

    def CheckGameOver(self):
        if self.n_strikes == 0:
            return True
        if self.score == len(self.numbers):
            return True
        return False

    def NextTurn(self):
        start_state = self.GetState()
        print(f"Player {self.acting_player_index + 1}'s turn to act.")
        print("Here's what they know about the game:")
        print(self.GetState(self.acting_player_index))
        self.Action()
        #self.GetActingPlayer().Act()
        self.over = self.CheckGameOver()
        self.acting_player_index = self.GetNextPlayerIndex()
        end_state = self.GetState()
        assert start_state != end_state
        return end_state

    def Action(self):
        while True:
            try:
                guessed_number = int(input("Guess a number 0-9> "))
                assert guessed_number in range(0,9)
                break
            except ValueError: # not an int
                continue
            except AssertionError: # not 0-9
                continue
        if self.NumberIsPlayable(guessed_number):
            print("Correct!")
            self.score += 1
        else:
            self.n_strikes -= 1
            print(f"Wrong. {self.n_strikes} strikes remaining.")



if __name__ == "__main__":

    game = Game()
    print(game.GetState())

    while not game.over:
        try:
            new_state = game.NextTurn()
            print(game.GetState())
        except AssertionError:
            print("Error: game state did not change when a turn was taken.")
            sys.exit(1)

    print("Game finished.")

    if game.score == len(game.numbers):
        print("Fireworks! You Win!")
    else:
        print("Too bad, you lose with a score of", game.GetScore())
