from collections import Counter
from constants import *
from util import card_combinations


class Hand(object):

    @staticmethod
    def get_successors(previous_play, current_hand, all_combos):
        """
        :return: a list of tuple (prev_play_type, prev_card_list)
        """
        prev_play_type, prev_card_list = previous_play
        if all_combos is not None:
            current_hand = Counter(current_hand)
            successors = []
            for combo_type, combo in all_combos:
                intersection = (Counter(combo) & Counter(current_hand)).elements()
                if len(list(intersection)) == len(list(combo)):
                    if prev_play_type == PASS:
                        successors.append((combo_type, combo))
                    elif combo_type == BOMB:
                        if prev_play_type == BOMB:
                            if combo[0] > prev_card_list[0]:
                                successors.append((combo_type, combo))
                        elif prev_play_type != KING_BOMB:
                            successors.append((combo_type, combo))
                    elif combo_type == KING_BOMB:
                        successors.append((combo_type, combo))
                    elif combo_type == prev_play_type and combo[0] > prev_card_list[0] and \
                            len(list(combo)) == len(prev_card_list):
                        successors.append((combo_type, combo))
            successors.append((PASS, ()))
            if prev_play_type == PASS:
                successors = [s for s in successors if s != (PASS, ())]
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
    def get_combo_type(previous_play, card_input, combos):
        if card_input == PASS:
            return PASS, ()
        successors = Hand.get_successors(previous_play, card_input, combos)
        for successor_type, successor_list in successors:
            if len(successor_list) == len(card_input):
                return successor_type, card_input
        raise ValueError('Invalid Play')
