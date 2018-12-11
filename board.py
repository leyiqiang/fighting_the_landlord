from constants import *
import random
from util import CardCombinations, deal
from collections import Counter
from hand import Hand


class BoardData(object):
    def __init__(self, prev_data=None):
        if prev_data is not None:
            self.base_card = prev_data.base_card  # the card landlord holds
            self.discarded_card = prev_data.discarded_card  # discarded cards
            self.previous_play = prev_data.previous_play
            self.agent_order = prev_data.agent_order
            self.turn = prev_data.turn
            self.pass_count = prev_data.pass_count
            self.card_combinations = prev_data.card_combinations
            self.is_terminal = prev_data.is_terminal
            self.winner = prev_data.winner
            self.hands = prev_data.hands
            self.combos = prev_data.combos
        else:
            self.base_card = []  # the card landlord holds
            self.discarded_card = []  # discarded cards
            self.previous_play = (PASS, [])
            farmer_order = random.sample([FARMER_ONE, FARMER_TWO], 2)
            self.agent_order = [LANDLORD] + farmer_order
            self.turn = LANDLORD
            self.pass_count = 0
            self.card_combinations = CardCombinations()
            self.is_terminal = False
            self.winner = None
            base_card, pile_one, pile_two, pile_three = deal()
            self.hands = {
                LANDLORD: base_card + pile_one,
                FARMER_ONE: pile_two,
                FARMER_TWO: pile_three,
            }
            self.combos = {
                LANDLORD: Hand.get_all_combos(self.hands[LANDLORD]),
                FARMER_ONE: Hand.get_all_combos(self.hands[FARMER_ONE]),
                FARMER_TWO: Hand.get_all_combos(self.hands[FARMER_TWO]),
            }

    def copy(self, BoardClass):
        state = BoardClass(self)
        state.base_card = self.base_card
        state.discarded_card = self.discarded_card
        state.previous_play = self.previous_play
        state.agent_order = self.agent_order
        state.turn = self.turn
        state.pass_count = self.pass_count
        state.is_terminal = self.is_terminal
        state.winner = self.winner
        state.hands = self.hands.copy()
        self.combos = self.combos.copy()
        return state

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
        current_turn_index = self.agent_order.index(self.turn)
        return self.agent_order[(current_turn_index + 1) % 3]

    def get_hands(self, agent_id):
        return self.hands[agent_id]

    def is_win(self, agent_id):
        if agent_id == FARMER_ONE or agent_id == FARMER_TWO:
            is_win = self.is_terminal and \
                     (len(self.get_hands(FARMER_ONE)) == 0 or
                      len(self.get_hands(FARMER_TWO)) == 0)
            return is_win
        else:
            return self.is_terminal and len(self.get_hands(LANDLORD)) == 0

    def is_loose(self, agent_id):
        if agent_id == LANDLORD:
            return self.is_terminal and len(self.get_hands(LANDLORD)) > 0
        else:
            return self.is_terminal and len(self.get_hands(FARMER_ONE)) > 0 and len(self.get_hands(FARMER_TWO)) > 0

    def get_position(self, agent_id):
        pos = self.agent_order.index(agent_id)
        return pos

    """
    make sure the hash are the same if the state is the same
    """
    def formalize(self, agent_id):
        return tuple(sorted(self.hands[agent_id]))
        # return tuple(sorted(self.hands[LANDLORD])), \
        #        tuple(sorted(self.hands[FARMER_ONE])), \
        #        tuple(sorted(self.hands[FARMER_TWO]))


class GameBoardData(BoardData):
    def next_state(self, action):
        next_state = self.copy(GameBoardData)
        play_type, card_list = action
        card_left = Counter(self.get_hands(self.turn)) - Counter(card_list)
        if len(card_left) == 0:
            next_state.is_terminal = True
            next_state.winner = self.turn
        if play_type == PASS and self.pass_count < 1:
            next_state.pass_count += 1
            next_state.turn = self.get_next_player()
            return next_state
        if play_type != PASS:
            next_state.pass_count = 0
        next_state.previous_play = (play_type, card_list)
        next_state.hands[self.turn] = list(card_left.elements())
        next_state.turn = self.get_next_player()
        next_state.discarded_card = self.discarded_card + list(card_list)
        return next_state

    def get_actions(self, agent_id=None):
        if self.is_terminal:
            return []
        if agent_id is None:
            agent_id = self.turn
        current_hand = self.get_hands(agent_id)
        actions = Hand.get_successors(self.previous_play, current_hand, self.combos[agent_id])
        return actions


class NonDeterministicBoardData(BoardData):
    def next_state(self, action):
        pass

    def get_actions(self, agent_id):
        pass
