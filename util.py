from constants import *
import itertools
import sys
import inspect
import random


class CardCombinations(object):

    def __init__(self):
        self._single = set()
        self._pair = set()
        self._trio = set()
        self._chain = set()
        self._pairs_chain = set()
        self._trio_single = set()
        self._trio_pair = set()
        self._airplane = set()
        self._airplane_small = set()
        self._airplane_large = set()
        self._four_with_two = set()
        self._four_with_pairs = set()
        self._bomb = set()
        self._king_bomb = set()
        self._card_types = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A, TWO, BLACK_JOKER, RED_JOKER]
        self._card_types_for_chain = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A]
        self.get_all_combinations()

    def __iter__(self):
        yield from {
            SINGLE: self._single,
            PAIR: self._pair,
            TRIO: self._trio,
            CHAIN: self._chain,
            PAIRS_CHAIN: self._pairs_chain,
            TRIO_SINGLE: self._trio_single,
            TRIO_PAIR: self._trio_pair,
            AIRPLANE: self._airplane,
            AIRPLANE_SMALL: self._airplane_small,
            AIRPLANE_LARGE: self._airplane_large,
            FOUR_WITH_TWO: self._four_with_two,
            FOUR_WITH_PAIRS: self._four_with_pairs,
            BOMB: self._bomb,
            KING_BOMB: self._king_bomb
        }.items()

    def get_all_combinations(self):
        for c in self._card_types:
            self._single.add((c,))
            if c < BLACK_JOKER:
                self._pair.add((c,) * 2)
                self._trio.add((c,) * 3)
                self._bomb.add((c,) * 4)
        self._king_bomb.add((BLACK_JOKER, RED_JOKER))
        # chain
        for i in range(0, len(self._card_types_for_chain)):
            for j in range(i + 5, len(self._card_types_for_chain)):
                self._chain.add(tuple(self._card_types_for_chain[i:j]))
        # pairs chain
        for i in range(0, len(self._card_types_for_chain)):
            for j in range(i + 3, len(self._card_types_for_chain)):
                sorted_list = sorted(self._card_types_for_chain[i:j] * 2)
                self._pairs_chain.add(tuple(sorted_list))
        # trio with single card
        for t in self._trio:
            for c in self._card_types:
                if t[0] != c:
                    self._trio_single.add(t + (c,))
        # trio with pairs
        for t in self._trio:
            for p in self._pair:
                if t[0] != p[0]:
                    self._trio_pair.add(t + p)
        # four with two cards
        two_cards_combinations = itertools.combinations(self._card_types, 2)
        for b in self._bomb:
            for c in two_cards_combinations:
                if b[0] != c[0] and b[0] != c[1]:
                    self._four_with_two.add(b + c)
        # bomb with pairs
        for b in self._bomb:
            for p in self._pair:
                if b[0] != p[0]:
                    self._four_with_pairs.add(b + p)

        # airplane combos
        for i in range(0, len(self._card_types_for_chain)):
            for j in range(i + 2, len(self._card_types_for_chain)):
                sorted_list = sorted(self._card_types_for_chain[i:j] * 3)
                tuple_sorted_list = tuple(sorted_list)
                # airplane
                if len(sorted_list) <= 20:
                    self._airplane.add(tuple_sorted_list)
                # airplane with small wings
                if len(sorted_list) + (j - i) <= 20:
                    for c in itertools.combinations(self._card_types, j - i):
                        if len(set(c).intersection(tuple_sorted_list)) == 0:
                            self._airplane_small.add(tuple_sorted_list + c)
                # airplane with large wings
                if len(sorted_list) + (j - i) * 2 <= 20:
                    for c in itertools.combinations(self._card_types, j - i):
                        if len(set(c).intersection(tuple_sorted_list)) == 0:
                            self._airplane_large.add(tuple_sorted_list + c * 2)


card_combinations = dict(CardCombinations())


def raise_not_defined():
    file_name = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, file_name))
    sys.exit(1)


def deal():
    deck_without_joker = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A, TWO] * 4
    deck = deck_without_joker + [BLACK_JOKER, RED_JOKER]
    random.shuffle(deck)
    # create three public cards for landlord
    base_card = deck[0:3]
    # deal deck into 17 cards
    pile_one = deck[3: 20]
    pile_two = deck[20: 37]
    pile_three = deck[37: 54]
    return base_card, pile_one, pile_two, pile_three
