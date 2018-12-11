"""
Card types:
single
pair
trio
chain(5 or more consecutive numbered cards)
pairs chain(3 or more consecutive pairs)
trio with single card
trio with pair
airplane(two or more consecutive trios)
airplane with small wings: two or more consecutive trios, with additional cards with the same amount of trios as kicker
airplane with large wings: two or more consecutive trios, with pairs with the same amount of trios as kicker
four with two single cards: four-of-a-kind, with two individual cards as kicker
four with two pairs: four-of-a-kind, with two pairs as kicker
bomb: four cards of the same rank
king bomb: respectively – colored joker with black-and-white joker cards
"""

SINGLE = 'SINGLE'
PAIR = 'PAIR'
TRIO = 'TRIO'
CHAIN = 'CHAIN'  # 5 or more consecutive numbered cards
PAIRS_CHAIN = 'PAIRS_CHAIN'  # 5 or more consecutive numbered pairs
TRIO_SINGLE = 'TRIO_SINGLE'  # trio with single card
TRIO_PAIR = 'TRIO_PAIR'  # trio with pair
AIRPLANE = 'AIRPLANE'  # two or more consecutive trios
# two or more consecutive trios, with additional cards with the same amount of trios as kicker
AIRPLANE_SMALL = 'AIRPLANE_SMALL'
# two or more consecutive trios, with pairs with the same amount of trios as kicker
AIRPLANE_LARGE = 'AIRPLANE_LARGE'
# four-of-a-kind, with two individual cards as kicker
FOUR_WITH_TWO = 'FOUR_WITH_TWO'
# four-of-a-kind, with two pairs as kicker
FOUR_WITH_PAIRS = 'FOUR_WITH_PAIRS'
# four cards of the same rank, can be played anytime(as long as previous bomb is smaller)
BOMB = 'BOMB'
# colored joker with black-and-white joker cards (biggest bomb)
KING_BOMB = 'KING_BOMB'

PASS = 'PASS'


"""
Card values:
Red Joker > Black Joker > 2 > A > K > Q > J ...
Color doesn't matter
Bombs can be played anytime
"""
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

"""
evaluate the utility of each card
"""
card_rating = {
    THREE: -6,
    FOUR: -5,
    FIVE: -4,
    SIX: -3,
    SEVEN: -2,
    EIGHT: -1,
    NINE: 0,
    TEN: 1,
    J: 2,
    Q: 3,
    K: 4,
    A: 5,
    TWO: 6,
    BLACK_JOKER: 7,
    RED_JOKER: 8
}

card_pretty_name = {
    THREE: '3',
    FOUR: '4',
    FIVE: '5',
    SIX: '6',
    SEVEN: '7',
    EIGHT: '8',
    NINE: '9',
    TEN: '10',
    J: 'J',
    Q: 'Q',
    K: 'K',
    A: 'A',
    TWO: '2',
    BLACK_JOKER: 'BlackJoker',
    RED_JOKER: 'RedJoker'
}
"""
Rounds
"""
LANDLORD = 'LANDLORD'
FARMER_ONE = 'FARMER_ONE'
FARMER_TWO = 'FARMER_TWO'

"""
Types of Policies
"""
RANDOM = 'random'
LONGEST_COMBO = 'longest_combo'
EVALUATION = 'evaluation'
CARD_VALUE = 'card_value'

"""
Types of Agents
"""
MCT_AGENT = 'MCTAgent'
ALPHA_BETA_AGENT = 'AlphaBetaAgent'
