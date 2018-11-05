from constants import *


class CardCombinations(object):

    def __init__(self):
        self.single = [] # done
        self.pair = [] # done
        self.trio = [] # done
        self.chain = [] # done
        self.pairs_chain = [] # done
        self.trio_single = [] # DONE
        self.trio_pair = [] # done
        self.airplane = [] # done
        self.airplane_small = []
        self.airplane_large = []
        self.four_with_two = []
        self.four_with_pairs = [] # done
        self.bomb = [] # done
        self.king_bomb = [] # done
        self.card_types = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, TWO, BLACK_JOKER, RED_JOKER]
        self.card_types_for_chain = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K]
        self.card_combinations = None


    def get_all_combinations(self):
        for c in self.card_types:
            self.single.append([c])
            if c < BLACK_JOKER:
                self.pair.append([c] * 2)
                self.trio.append([c] * 3)
                self.bomb.append([c] * 4)
        self.king_bomb.append([BLACK_JOKER, RED_JOKER])
        # chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 5, len(self.card_types_for_chain)):
                self.chain.append(self.card_types_for_chain[i:j])
        # pairs chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 3, len(self.card_types_for_chain)):
                self.pairs_chain.append(sorted(self.card_types_for_chain[i:j] * 2))
        # trios chain (airplane)
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 2, len(self.card_types_for_chain)):
                if (j - i) * 3 <= 20:
                    self.airplane.append(sorted(self.card_types_for_chain[i:j] * 3))
        # trio with single card
        for t in self.trio:
            for c in self.card_types:
                if t[0] != c:
                    self.trio_single.append(t + [c])
        # trio with pairs
        for t in self.trio:
            for p in self.pair:
                if t[0] != p[0]:
                    self.trio_pair.append(t + p)
        # four with two cards # todo
        for b in self.bomb:
            for c in self.card_types:
                if b[0] != c:
                    self.four_with_two.append(b + [c])
        # bomb with pairs
        for b in self.bomb:
            for p in self.pair:
                if b[0] != p[0]:
                    self.four_with_pairs.append(b + p)

        #todo airplanes

        self.card_combinations = {
            SINGLE: to_set(self.single),
            PAIR: to_set(self.pair),
            TRIO: to_set(self.trio),
            CHAIN: to_set(self.chain),
            PAIRS_CHAIN: to_set(self.pairs_chain),
            TRIO_SINGLE: to_set(self.trio_single),
            TRIO_PAIR: to_set(self.trio_pair),
            AIRPLANE: to_set(self.airplane),
            AIRPLANE_SMALL: to_set(self.airplane_small),
            AIRPLANE_LARGE: to_set(self.airplane_large),
            FOUR_WITH_TWO: to_set(self.four_with_two),
            FOUR_WITH_PAIRS: to_set(self.four_with_pairs),
            BOMB: to_set(self.bomb),
            KING_BOMB: to_set(self.king_bomb)
        }
        print(self.card_combinations)


def to_set(list):
    return set(tuple(x) for x in list)