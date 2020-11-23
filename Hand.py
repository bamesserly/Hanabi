from Deck import Deck
from Card import Card

class Hand:
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.DealOneCard())

    def GetCode(self):
        return "".join(c.GetCode() for c in self.cards)

    def ReplaceCard(self, card_idx, deck):
        assert card_idx in range(5)
        old = self.cards[card_idx]
        try:
            self.cards[card_idx] = deck.DealOneCard()
        except AssertionError:
            print("Deck empty, still removing old card, but not replacing it with anything.")
            self.cards[card_idx] = None
        return old

if __name__ == "__main__":
    d = Deck()
    h = Hand(d)
    print(h.GetCode())
    old = h.ReplaceCard(1, d)
    print("Getting rid a ...", old.GetCode(), "and drawing a new card from the deck")
    print(h.GetCode())
