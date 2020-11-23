from Card import Card
from random import random

class Deck:
    n_cards = 50

    def __init__(self):
        self.cards = []
        for i in range (self.n_cards):
            self.cards.append(Card(i))
        self.Shuffle()
        self.next_card_idx = 0 # top card is 0th card

    # TODO
    def Shuffle(self):
        pass
        #for i in range(self.n_cards):
        #    j = i + random() % (self.n_cards - i)
        #    print(j)
        #    j = int(j)
        #    tmp = self.cards[i]
        #    self.cards[i] = m_cards[j];
        #    self.cards[j] = tmp

    def Size(self):
        return self.n_cards - self.next_card_idx

    def DealOneCard(self):
        try:
            assert self.next_card_idx in range(self.n_cards)
            c = self.cards[self.next_card_idx]
            self.next_card_idx += 1
            return c
        except AssertionError:
            pass

    def GetCode(self):
        return "".join(c.GetCode() for c in self.cards[self.next_card_idx:self.n_cards])

if __name__ == "__main__":
    d = Deck()
    while d.Size() > 0:
        print(d.DealOneCard().GetCode())
