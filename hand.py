from collections import Counter
from constants import *


class Hand(object):
    def __init__(self, card_list):
        self._card_list = tuple(sorted(card_list))
        self._card_set = set(self._card_list)
        self._single = []
        self._pair = []
        self._trio = []
        self._bomb = []
        self._king_bomb = []
        self._chain = []
        self._is_pass = False
        self._counter = Counter(card_list)

    def get_successors(self, board):
        """
        :param board: an Object that keeps track of state of the game
        :return: a list of tuple (play_type, card_list, cards_left)
        """
        successors = []
        play_type, card_list = board.previous_play
        card_combinations = board.card_combinations
        for k, v in card_combinations.items():
            if k == play_type or play_type == PASS:
                for combo in v:
                    intersection = set(combo).intersection(self._card_set)
                    if len(intersection) == len(combo):
                        successors.append((k, combo, self.get_cards_left(combo)))
        return successors

    def get_cards_left(self, card_list):
        return self._card_set - set(card_list)