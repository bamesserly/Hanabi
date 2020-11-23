from Card import Card
from Deck import Deck
from Player import Player

class Game:
    def __init__(self, n_players = 2):
        self.over = False
        self.n_fuses = 3
        self.n_clocks = 8
        self.deck = Deck()
        self.players = []
        self.acting_player = 0
        for i in range(n_players):
            self.players.append(Player(self))
        self.piles = {}
        for suit in Card.suits:
            self.piles[suit] = 0
        self.discard = []
        self.state = self.GetState()

    def GetActingPlayer(self):
        return self.players[self.acting_player]

    def NextTurn(self):
        start_state = self.GetState()
        self.GetActingPlayer().Act(self)
        self.over = self.CheckGameOver()
        self.acting_player = (self.acting_player + 1) % len(self.players)
        end_state = self.GetState()
        assert start_state != end_state
        return end_state

    def CheckGameOver(self):
        if self.n_fuses == 0:
            return True
        if self.deck.Size() == 0:
            return True
        if all(i == 5 for i in self.piles.values()):
            return True
        return False

    def GetState(self):
        self.state = str(self.n_fuses) + str(self.n_clocks)
        self.state += str(self.acting_player)
        for key, val in self.piles.items():
            self.state += key + str(val)
        self.state += self.deck.GetCode()
        for p in self.players:
            self.state += p.hand.GetCode()
        return self.state

if __name__ == "__main__":
    g = Game()
    print(g.GetState())
