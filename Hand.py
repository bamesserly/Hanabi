from Deck import Deck
from Card import Card


class Hand:

    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.DrawCard())

    def GetCode(self):
        return "".join(c.GetCode() for c in self.cards)

    # Draw a card from the deck, place it in the card_idx slot and return
    # the removed card
    def ReplaceCard(self, card_idx, deck):
        assert card_idx in range(5)
        old = self.cards[card_idx]
        try:
            self.cards[card_idx] = deck.DrawCard()
        except AssertionError:
            print(
                "Hand::ReplaceCard: Deck empty, still removing old card, "
                "but not replacing it with anything."
            )
            self.cards[card_idx] = None
        return old

    def HasValidCard(self, card_idx):
        return self.cards[card_idx] is not None

    def PromptCardSelection(self, play_or_discard = "play"):
        while True:
            which_card = int(input(f"Select a card (specify 0-4) to {play_or_discard}>\n"))
            if which_card in range(5):
                try:
                    assert self.HasValidCard(which_card)
                except AssertionError:
                    print("Your hand has no such card, choose again.")
                break
            print("Range is not allowed!")
        return which_card


if __name__ == "__main__":
    d = Deck()
    h = Hand(d)
    print(h.GetCode())
    print("Replace a card with one from the deck.")
    which_card = h.PromptCardSelection()
    old = h.ReplaceCard(which_card, d)
    print("Getting rid of ...", old.GetCode(), "and drawing a new card from the deck")
    print(h.GetCode())
