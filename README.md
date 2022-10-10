# Terminal Poker Night
This is a simple Python3 implementation of a classic "Jacks or better" style video poker machine. No external packages needed.

# How to play
## Startup

The game starts by running `videopoker.py`
First, you will be prompted for the amount of tokens you wish to deposit, and the amount you will be betting each round.

## Gameplay

Your goal is to score the best possible Poker hand.
Five cards will be drawn.
You have the option to either keep or discard any of the five initial cards.
Discarded cards will be replaced by new cards from the deck.

Choosing to keep the cards is done by supplying each number representing the card. For example, keeping cards 1 and 4 is done by inputting `14`

Once the final set of cards is visible, the Poker hand is calculated. Additional tokens will be rewarded for winning hands, based on the hand and the size of the bet.