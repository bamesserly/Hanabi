from Card import Card
from Hand import Hand



class Player:

    def __init__(self, game, idx):
        self.game = game
        self.idx = idx
        self.hand = Hand(self.game.deck)
        self.knowledge = {0: "XX", 1: "XX", 2: "XX", 3: "XX", 4: "XX"}


    def Act(self):
        # Choose to (a) give info, (b) discard, or (c) play
        while True:
            which_action = input(
                "Choose: (a) give information, (b) discard, or (c) play a card.\n"
            ).lower()
            if which_action in ["a", "b", "c"]:
                if which_action == "a" and self.game.n_clocks == 0:
                    print("Not enough clocks to give information.")
                else:
                    break

        # Give info
        if which_action == "a":
            self.game.n_clocks -= 1

            # Choose player
            if len(self.game.players) == 2:
                which_player = not int(self.idx)
            else:
                while True:
                    which_player = (
                        int(input("To which player would you like to give info?\n")) - 1
                    )
                    if (
                        which_player in range(len(self.game.players))
                        and which_player != self.idx
                    ):
                        break
                    else:
                        print("Cannot give information to this player.")

            # Choose the info
            while True:
                which_info = input(
                    "\nWhat info do you want to give to this player?\n Choose "
                    "among R, Y, W, G, B, 1, 2, 3, 4, 5.\n"
                ).upper()
                if which_info in Card.suits or int(which_info) in Card.values:
                    break
                else:
                    print("Not a valid info choice.")

            self.game.players[which_player].AddKnowledge(which_info)

        # Discard
        elif which_action == "b":
            which_card = self.hand.PromptCardSelection("discard")
            self.ClearCardKnowledge(which_card)
            self.DiscardAndDrawNew(which_card)
            self.game.n_clocks += 1

        # Play
        elif which_action == "c":
            which_card = self.hand.PromptCardSelection("play")
            self.ClearCardKnowledge(which_card)
            card = self.hand.ReplaceCard(which_card, self.game.deck)
            if self.game.CardIsPlayable(card.idx):
                self.game.piles[card.GetSuit()] += 1
                print("Successfully played a card! Nice!")
            else:
                self.game.discard_pile.AddCard(card)
                self.game.n_fuses -= 1
                print(
                    "Fail! Unable to play",
                    card.GetCode(),
                    ".",
                    self.game.n_fuses,
                    "fuses remaining.",
                )


    def DiscardAndDrawNew(self, card_idx):
        # Remove discarded card from hand and draw a new from deck
        old_card = self.hand.ReplaceCard(card_idx, self.game.deck)

        # Add old card to discard pile
        self.game.discard_pile.AddCard(old_card)


    # Add color or value info to your knowledge 
    def AddKnowledge(self, info):
        # loop your cards
        for idx, c in enumerate(self.hand.cards):
            # info provided is a suit
            if info in Card.suits and info == c.GetSuit():
                know = list(self.knowledge[idx]) # e.g. ['Y', 5]
                know[0] = info
                self.knowledge[idx] = "".join(know)
            # info provided is a value
            try:
                if int(info) in Card.values and int(info) == c.GetValue():
                    know = list(self.knowledge[idx])
                    know[1] = info
                    self.knowledge[idx] = "".join(know)
            except ValueError:
                pass


    # Clear the knowledge of a specific card in your hand (because you
    # discarded or played it). Specify card by its index in your hand.
    # self.knowledge = {0: "XX", 1: "XX", 2: "XX", 3: "XX", 4: "XX"}
    def ClearCardKnowledge(self, which_card):
        self.knowledge[which_card] = "XX"


if __name__ == "__main__":
    pass
