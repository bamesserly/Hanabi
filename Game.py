from Card import Card
from Deck import Deck

class Game:
    def __init__(self):
        self.over = False
        self.n_fuses = 3
        self.n_clocks = 8
        self.deck = Deck()
        self.state = self.GetState()

    def NextTurn(self):
        self.deck.DealOneCard()
        self.over = self.CheckGameOver()

    def CheckGameOver(self):
        if self.n_fuses == 0:
            return True
        if self.deck.Size() == 0:
            return True
        # TODO if win:
            return True
        return False

    def GetState(self):
        self.state = str(self.n_fuses) + str(self.n_clocks)
        self.state += self.deck.GetCode()
        return self.state
