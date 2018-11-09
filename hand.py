from collections import Counter
from constants import *
from util import card_combinations


class Hand(object):

    @staticmethod
    def get_successors(previous_play, current_hand, all_combos):
        """
        :return: a list of tuple (play_type, card_list)
        """
        if all_combos is not None:
            current_hand = Counter(current_hand)
            successors = []
            play_type, card_list = previous_play
            for combo_type, combo in all_combos:
                if combo_type == play_type or play_type == PASS:
                    intersection = (Counter(combo) & Counter(current_hand)).elements()
                    if len(list(intersection)) == len(list(combo)):
                        if play_type == PASS or combo[0] > card_list[0]:
                            successors.append((combo_type, combo))
            if play_type != PASS:
                successors.append((PASS, ()))
            return successors

    @staticmethod
    def get_all_combos(initial_hand):
        current_hand = Counter(initial_hand)
        successors = []
        for combo_type, combo_list in card_combinations.items():
            for combo in combo_list:
                intersection = (Counter(combo) & Counter(current_hand)).elements()
                if len(list(intersection)) == len(combo):
                    successors.append((combo_type, combo))
        successors.append((PASS, ()))
        return successors

    # def get_cards_left(self, card_list):
    #     counter = self._card_counter - Counter(card_list)
    #     return list(counter.elements())
    @staticmethod
    def get_combo_type(previous_play, card_input):
        # current_hand = Counter(card_list)
        play_type, card_list = previous_play
        if card_input[0] == PASS:
            return PASS
        for combo_type, combo_list in card_combinations.items():
            for combo in combo_list:
                if combo == card_input and (play_type == PASS or card_list[0] < card_input[0]):
                    return combo_type
        raise ValueError('Invalid Play')
