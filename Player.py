from Hand import Hand

class Player:
    def __init__(self, game):
        self.hand = Hand(game.deck)
        self.knowledge = {1 : {}, 2 : {}, 3 : {}, 4 : {}, 5 : {}}

    def Act(self, game):
        game.deck.DealOneCard()

    def Discard(self, game, card_idx):
        game.discard_pile.append(self.hand.cards[card_idx])
