from collections import Counter
from constants import *
from util import card_combinations


class Hand(object):

    @staticmethod
    def get_successors(previous_play, current_hand, all_combos):
        """
        :return: a list of tuple (prev_play_type, prev_card_list)
        """
        if all_combos is not None:
            current_hand = Counter(current_hand)
            successors = []
            prev_play_type, prev_card_list = previous_play
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
            return successors

    """
    A function used for non-deterministic environment
    """
    def get_possible_successors(self, previous_play, visible_cards, discarded_cards):
        pass

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
        # current_hand = Counter(card_list)
        play_type, card_list = previous_play
        if card_input == PASS:
            return PASS, ()
        # for combo_type, combo_list in card_combinations.items():
            # for combo in combo_list:
                # if sorted(list(card_input)) == sorted(list(combo)):
        successors = Hand.get_successors(previous_play, card_input, combos)
        for successor_type, successor_list in successors:
            if len(successor_list) == len(card_input):
                return successor_type, card_input
                    # if play_type == PASS or card_list[0] < combo[0]:
                    #     return combo_type, combo
                    # if play_type not in [BOMB, KING_BOMB] and combo_type in [BOMB, KING_BOMB]:
                    #     return combo_type, combo

        raise ValueError('Invalid Play')
