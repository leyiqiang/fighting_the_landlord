from constants import *
import random
from util import CardCombinations
import sys


class Board(object):
    # track the state of the game
    def __init__(self):
        deck_without_joker = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A, TWO] * 4
        self._deck = deck_without_joker + [BLACK_JOKER, RED_JOKER]
        self._base_card = []  # the card landlord holds
        self._discarded_card = []  # discarded cards
        self._previous_play = (PASS, [])
        self._agent_order = [FARMER_ONE, FARMER_TWO, LANDLORD]
        random.shuffle(self._agent_order)
        self._current_round = 0
        self._pass_count = 0
        self._card_combinations = CardCombinations()

    @property
    def base_card(self):
        return self._base_card

    @property
    def discarded_card(self):
        return self._discarded_card

    @property
    def previous_play(self):
        return self._previous_play

    @property
    def agent_order(self):
        return self._agent_order

    @property
    def agent_order_pretty(self):
        pretty_order = []
        for o in self._agent_order:
            if o == FARMER_ONE:
                pretty_order.append('farmer1')
            if o == FARMER_TWO:
                pretty_order.append('farmer2')
            if o == LANDLORD:
                pretty_order.append('landlord')
        return pretty_order

    @property
    def current_round(self):
        return self._current_round

    @property
    def card_combinations(self):
        return dict(self._card_combinations)

    def deal(self):
        random.shuffle(self._deck)
        # create three public cards for landlord
        self._base_card = self._deck[0:3]
        # deal deck into 17 cards
        pile_one = self._deck[3: 20]
        pile_two = self._deck[20: 37]
        pile_three = self._deck[37: 54]
        return pile_one, pile_two, pile_three

    def play(self, action, player):
        print('{0} plays {1}'.format(player, action))
        play_type, card_list, len_card_left = action
        if play_type == PASS and self._pass_count < 2:
            self._pass_count += 1
        if self._pass_count < 2:
            return
        self._previous_play = (play_type, card_list)
        self._discard(card_list)
        if len_card_left == 0:
            print('*** GAME OVER, {0} WIN ***'.format(player))
            sys.exit(0)

    def _discard(self, card_list):
        self._discarded_card.append(card_list)
