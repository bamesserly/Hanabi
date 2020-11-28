################################################################################
# CardPiles are just lists of integers, and it is assumed that the integer has
# a corresponding Card object, from which a code can be extracted.
################################################################################
from Card import Card
import random


class CardPile:

    def __init__(self):
        self.cards = []

    def Size(self):
        return len(self.cards)

    def GetCode(self):
        return "".join(c.GetCode() for c in self.cards)


class Discard(CardPile):

    def __init__(self):
        super().__init__()

    def AddCard(self, c):
        self.cards.insert(0, c)


class Deck(CardPile):
    n_cards = int(len(Card.suits) * len(Card.values))  # 50, for normal deck

    def __init__(self):
        super().__init__()
        for i in range(self.n_cards):
            self.cards.append(Card(i))
        self.Shuffle()

    def Shuffle(self):
        random.shuffle(self.cards)

    def DrawCard(self):
        try:
            c = self.cards.pop(0)
            return c
        except IndexError:
            print("Deck::DrawCard: no more cards to draw")
            return None


if __name__ == "__main__":
    deck = Deck()
    discard = Discard()
    print(deck.GetCode())
    while deck.Size() > 0:
        c = deck.DrawCard()
        discard.AddCard(c)
        print(deck.GetCode(), " | ", discard.GetCode())
