from constants import *
import itertools


class CardCombinations(object):

    def __init__(self):
        self.single = set() # done
        self.pair = set() # done
        self.trio = set() # done
        self.chain = set() # done
        self.pairs_chain = set() # done
        self.trio_single = set() # DONE
        self.trio_pair = set() # done
        self.airplane = set() # done
        self.airplane_small = set()
        self.airplane_large = set()
        self.four_with_two = set()
        self.four_with_pairs = set() # done
        self.bomb = set() # done
        self.king_bomb = set() # done
        self.card_types = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, TWO, BLACK_JOKER, RED_JOKER]
        self.card_types_for_chain = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K]
        self.card_combinations = None

    def get_all_combinations(self):
        for c in self.card_types:
            self.single.add((c,))
            if c < BLACK_JOKER:
                self.pair.add((c,) * 2)
                self.trio.add((c,) * 3)
                self.bomb.add((c,) * 4)
        self.king_bomb.add((BLACK_JOKER, RED_JOKER))
        # chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 5, len(self.card_types_for_chain)):
                self.chain.add(tuple(self.card_types_for_chain[i:j]))
        # pairs chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 3, len(self.card_types_for_chain)):
                sorted_list = sorted(self.card_types_for_chain[i:j] * 2)
                self.pairs_chain.add(tuple(sorted_list))
        # trio with single card
        for t in self.trio:
            for c in self.card_types:
                if t[0] != c:
                    self.trio_single.add(t + (c,))
        # trio with pairs
        for t in self.trio:
            for p in self.pair:
                if t[0] != p[0]:
                    self.trio_pair.add(t + p)
        # four with two cards
        two_cards_combinations = itertools.combinations(self.card_types, 2)
        for b in self.bomb:
            for c in two_cards_combinations:
                if b[0] != c[0] and b[0] != c[1]:
                    self.four_with_two.add(b+c)
        print(self.four_with_two)
        # bomb with pairs
        for b in self.bomb:
            for p in self.pair:
                if b[0] != p[0]:
                    self.four_with_pairs.add(b + p)

        print(self.four_with_pairs)
        # airplane combos
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 2, len(self.card_types_for_chain)):
                sorted_list = sorted(self.card_types_for_chain[i:j] * 3)
                tuple_sorted_list = tuple(sorted_list)
                cards_combinations = itertools.combinations(self.card_types, j - i)
                # airplane
                if len(sorted_list) <= 20:
                    self.airplane.add(tuple_sorted_list)
                # airplane with small wings
                if len(sorted_list) + (j - i) <= 20:
                    for c in cards_combinations:
                        # todo check no duplicate
                        self.airplane_small.add(tuple_sorted_list + c)
                        print(tuple_sorted_list+c)
                # airplane with large wings
                if len(sorted_list) + (j - i) * 2 <= 20:
                    for c in cards_combinations:
                        # todo check no duplicate
                        self.airplane_large.add(tuple_sorted_list + c * 2)

        # print(self.airplane)
        # print(self.airplane_small)
        # print(self.airplane_large)
        # self.card_combinations = {
        #     SINGLE: to_set(self.single),
        #     PAIR: to_set(self.pair),
        #     TRIO: to_set(self.trio),
        #     CHAIN: to_set(self.chain),
        #     PAIRS_CHAIN: to_set(self.pairs_chain),
        #     TRIO_SINGLE: to_set(self.trio_single),
        #     TRIO_PAIR: to_set(self.trio_pair),
        #     AIRPLANE: to_set(self.airplane),
        #     AIRPLANE_SMALL: to_set(self.airplane_small),
        #     AIRPLANE_LARGE: to_set(self.airplane_large),
        #     FOUR_WITH_TWO: to_set(self.four_with_two),
        #     FOUR_WITH_PAIRS: to_set(self.four_with_pairs),
        #     BOMB: to_set(self.bomb),
        #     KING_BOMB: to_set(self.king_bomb)
        # }
        # print(self.card_combinations)

#
# def to_set(list):
#     return set(tuple(x) for x in list)