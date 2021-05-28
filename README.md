# Fighting the Landlord AI 基于Minimax和MCTS算法的两种斗地主
Playing Fighting the Landlord, a Chinese poker game using Minimax and MCTS algorithms.

基于Minimax和MCTS算法的两种斗地主.

## Installation
Python version 3.3 or above is required.
```
git clone https://github.com/leyiqiang/fighting_the_landlord.git
python ./game.py
```

## Usages

###Optional Arguments:

| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -l --landlord 	       |	ReflexAgent           |Agent used for landlord
| -f --farmer 	       |	ReflexAgent           |Agent used for the two farmers
| -e --evaluation 	       |	Random           |Rollout policy used for agents
| -d --debug 	       |	False           |Set debug mode of the program

###Agent Types:

**ReflexAgent**: Play cards automatically by randomly select available combos.

**ManualAgent**: Play cards by the user manually.

**MiniMaxAgent**: Play cards automatically using Minimax(without Alpha-Beta Pruning) algorithm.

**AlphaBetaAgent**: Play cards automatically using Minimax(with Alpha-Beta Pruning) algorithm.

**MCTAgent**: Play cards using MCTS algorithm (slow). 

###Rollout Policies:

**random**: randomly select plays.

**longest_combo**: select combo with the largest amount of cards.

**card_value**: select combo with highest sum of values (see card values in constants.py).

**evaluation**: select combo with highest sum of evaluation points(see card_rating in constants.py).

## How to Play (ManualAgent)
Play card numbers separated by commas, type "PASS" to pass current turn.

###Card values:
```
Red Joker > Black Joker > 2 > A > K > Q > J ...
Color doesn't matter
THREE = 0
FOUR = 1
FIVE = 2
SIX = 3
SEVEN = 4
EIGHT = 5
NINE = 6
TEN = 7
J = 8
Q = 9
K = 10
A = 11
TWO = 12
BLACK_JOKER = 13
RED_JOKER = 14
```

For example, if you want to play triple FIVE with a THREE in your turn, type
`2,2,2,0` in the command.
