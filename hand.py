from collections import Counter
from constants import *


class Hand(object):
    def __init__(self, card_list):
        self._card_list = sorted(card_list)
        self._card_counter = Counter(self._card_list)
        self._single = []
        self._pair = []
        self._trio = []
        self._bomb = []
        self._king_bomb = []
        self._chain = []
        self._is_pass = False

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, new_list):
        self._card_list = new_list

    def get_successors(self, previous_play, card_combinations):
        """
        :return: a list of tuple (play_type, card_list, cards_left)
        """
        successors = []
        play_type, card_list = previous_play
        card_combinations = card_combinations
        for combo_type, combo_list in card_combinations.items():
            if combo_type == play_type or play_type == PASS:
                for combo in combo_list:
                    intersection = (Counter(combo) & Counter(self._card_counter)).elements()
                    if len(list(intersection)) == len(combo):
                        successors.append((combo_type, combo, self.get_cards_left(combo)))
        successors.append(('PASS', (), self.get_cards_left(())))
        return successors

    def get_cards_left(self, card_list):
        counter = self._card_counter - Counter(card_list)
        return list(counter.elements())