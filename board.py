from constants import *
import random
from util import CardCombinations


class BoardData(object):
    # track the state of the game
    def __init__(self, prev_data=None):
        if prev_data:
            self.base_card = prev_data.base_card  # the card landlord holds
            self.discarded_card = prev_data.discarded_card  # discarded cards
            self.previous_play = prev_data.previous_play
            self.agent_order = prev_data.agent_order # todo
            self.current_turn = prev_data.current_turn
            self.pass_count = prev_data.pass_count
            self.card_combinations = prev_data.card_combinations
            self.is_terminal = prev_data.is_terminal
            self.winner = prev_data.winner
        else:
            self.base_card = []  # the card landlord holds
            self.discarded_card = []  # discarded cards
            self.previous_play = (PASS, [])
            farmer_order = random.sample([FARMER_ONE, FARMER_TWO], 2)
            self.agent_order = [LANDLORD] + farmer_order
            self.current_turn = LANDLORD
            self.pass_count = 0
            self.card_combinations = CardCombinations()
            self.is_terminal = False
            self.winner = None

    @property
    def agent_order_pretty(self):
        pretty_order = []
        for o in self.agent_order:
            if o == FARMER_ONE:
                pretty_order.append('farmer1')
            if o == FARMER_TWO:
                pretty_order.append('farmer2')
            if o == LANDLORD:
                pretty_order.append('landlord')
        return pretty_order

    def get_next_player(self):
        current_turn_index = self.agent_order.index(self.current_turn)
        return self.agent_order[(current_turn_index + 1) % 3]

    def copy(self):
        state = BoardData(self)

        state.base_card = self.base_card
        state.discarded_card = self.discarded_card
        state.previous_play = self.previous_play
        state.agent_order = self.agent_order
        state.current_turn = self.current_turn
        state.pass_count = self.pass_count
        state.is_terminal = self.is_terminal
        state.winnder = self.winner
        return state

    def next_state(self, action):
        next_state = self.copy()
        play_type, card_list, len_card_left = action
        if len_card_left == 0:
            next_state.is_terminal = True
            next_state.winner = self.current_turn
        if play_type == PASS and self.pass_count < 2:
            next_state.pass_count += 1
            return next_state
        next_state.previous_play = (play_type, card_list)
        next_state.current_turn = self.get_next_player()
        next_state.discarded_card = self.discarded_card + list(card_list)
        return next_state
