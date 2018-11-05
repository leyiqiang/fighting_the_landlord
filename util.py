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
        self.card_combinations = {
            SINGLE: [],
            PAIR: [],
            TRIO: [],
            CHAIN: [],
            PAIRS_CHAIN: [],
            TRIO_SINGLE: [],
            TRIO_PAIR: [],
            AIRPLANE: [],
            AIRPLANE_SMALL: [],
            AIRPLANE_LARGE: [],
            FOUR_WITH_TWO: [],
            FOUR_WITH_PAIRS: [],
            BOMB: [],
            KING_BOMB: []
        }


    def get_all_combinations(self):
        for c in self.card_types:
            self.single.append([c])
            if c < BLACK_JOKER:
                self.pair.append([c] * 2)
                self.trio.append([c] * 3)
                self.bomb.append([c] * 4)
        self.king_bomb.append([BLACK_JOKER, RED_JOKER])
        print(self.pair)
        print(self.trio)
        print(self.bomb)
        print(self.king_bomb)
        # chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 5, len(self.card_types_for_chain)):
                self.chain.append(self.card_types_for_chain[i:j])
        print(self.chain)
        # pairs chain
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 3, len(self.card_types_for_chain)):
                self.pairs_chain.append(sorted(self.card_types_for_chain[i:j] * 2))
        print(self.pairs_chain)
        # trios chain (airplane)
        for i in range(0, len(self.card_types_for_chain)):
            for j in range(i + 2, len(self.card_types_for_chain)):
                if (j - i) * 3 <= 20:
                    self.airplane.append(sorted(self.card_types_for_chain[i:j] * 3))
        print(self.airplane)
        # trio with single card
        for t in self.trio:
            for c in self.card_types:
                if t[0] != c:
                    self.trio_single.append(t + [c])
        print(self.trio_single)
        # trio with pairs
        for t in self.trio:
            for p in self.pair:
                if t[0] != p[0]:
                    self.trio_pair.append(t + p)
        print (self.trio_pair)
        # four with two cards # todo
        for b in self.bomb:
            for c in self.card_types:
                if b[0] != c:
                    self.four_with_two.append(b + [c])
        print(self.trio_single)
        # bomb with pairs
        for b in self.bomb:
            for p in self.pair:
                if b[0] != p[0]:
                    self.four_with_pairs.append(b + p)
        print (self.four_with_pairs)

        #todo airplanes