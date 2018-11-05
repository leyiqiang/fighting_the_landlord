from constants import *
import random


class Board(object):
    # track the state of the game
    def __init__(self):
        deck_without_joker = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A, TWO] * 4
        self._deck = deck_without_joker + [BLACK_JOKER, RED_JOKER]
        self._base_card = []  # the card landlord holds
        self._discarded_card = []  # discarded cards
        self._previous_play = (PASS, [])
        self._agent_order = random.shuffle([FARMER_ONE, FARMER_TWO, LANDLORD])
        self._current_round = 0

    @property
    def base_card(self):
        return self._base_card

    def deal(self):
        random.shuffle(self._deck)
        # create three public cards for landlord
        self._base_card = self._deck[0:3]
        # deal deck into 17 cards
        pile_one = self._deck[3: 20]
        pile_two = self._deck[20: 37]
        pile_three = self._deck[37: 54]
        return pile_one, pile_two, pile_three

    def discard(self, card_list):
        self._discarded_card.append(card_list)
