Hanabi!

Call Game::NextTurn until game.over.

A Game owns a Deck, Discard pile, list of Players, dictionary of played cards, and a 'state' string which encodes all info about the current state of the game.

Deck and Discard are both CardPiles -- a list of Cards. A Deck can additionally be Shuffled and a Card can be drawn from it.

A Card is just an integer [0-49] which uniquely maps to a (value, suit) pair. You can call GetSuit and GetValue to get its suit string (Red, Yellow, Blue, Green, White) and value integer (1-5).

A Hand is a list of five cards initally drawn from a Deck. A Hand can ReplaceCard by drawing one from a given Deck. And Hand has PromptCardSelection, which prompts the user to choose one of the cards.

A Player has their Hand can Act with one of up to three actions. Act-ing affects lots of aspects of the game, for example the Deck and Player knowledge.

-------------------------------------------------------------

Current Status: Run with `python Play.py`. Runs in god mode now, where you see the game state inbetween every move, but 'users' are still prompted for their action.
