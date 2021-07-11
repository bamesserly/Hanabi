from Card import Card
from Deck import Deck, Discard
from Player import Player


class Game:

    def __init__(self, n_players=2):
        print("Starting a new game.")
        self.over = False
        self.n_fuses = 3
        self.n_clocks = 8
        self.deck = Deck()
        self.players = []
        self.acting_player = 0
        for i in range(n_players):
            self.players.append(Player(self, i))
        self.piles = {suit: 0 for suit in Card.suits}
        for suit in Card.suits:
            self.piles[suit] = 0
        self.discard_pile = Discard()
        self.state = self.GetState()

    def GetActingPlayer(self):
        return self.players[self.acting_player]

    def NextTurn(self):
        start_state = self.GetState()
        print("Player", self.acting_player + 1, "'s turn to act.")
        print("Here's what they know about the game:")
        print(self.GetState(self.acting_player))
        self.GetActingPlayer().Act()
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

    def GetScore(self):
        return sum(self.piles.values())

    def CardIsPlayable(self, card):
        c = Card(card)
        if self.piles[c.GetSuit()] + 1 == c.GetValue():
            return True
        else:
            return False

    # List of info. Ultimately want to join.
    def GetState(self, player_idx=None):
        self.state = []
        self.state.append(str(self.n_fuses))
        self.state.append(str(self.n_clocks))
        self.state.append(str(self.acting_player))
        for key, val in self.piles.items():
            self.state.append(key + str(val))
        for idx, p in enumerate(self.players):
            if idx == player_idx:
                self.state.append("")
            else:
                self.state.append(p.hand.GetCode())
            self.state.append(p.knowledge)
        if player_idx is not None:
            self.state.append("")
        else:
            self.state.append(self.deck.GetCode())
        self.state.append(self.discard_pile.GetCode())
        return self.state


if __name__ == "__main__":
    g = Game()
    print("The game state encodes everything there is to know about the game:")
    print(g.GetState())
    c_idx = 2
    c = Card(c_idx)
    print("A", c.GetCode(), "is playable?", g.CardIsPlayable(c_idx))
