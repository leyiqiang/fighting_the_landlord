from agents import Agents, MultiAgentSearch
import random
from hand import Hand


class ReflexAgent(Agents):
    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        card_type, card_list = random.choice(actions)
        return card_type, card_list


class MiniMaxAgent(MultiAgentSearch):

    def __init__(self, agent_id):
        Agents.__init__(self, agent_id)
        self.max_depth = 3

    # successors is a list of tuple (play_type, card_list)
    def get_action(self, board_state):
        current_hand = board_state.get_hands(self.agent_id)
        actions = Hand.get_successors(board_state.previous_play, current_hand)
        max_val = float('-inf')
        for a in actions:
            next_state = board_state.next_state(a)
            min_val = self.get_min_value(self.agent_id, 0, next_state)
            if min_val > max_val:
                max_val = min_val
                next_state = a
        return next_state

    def get_min_value(self, agent, current_depth, current_state):
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state)


class AlphaBetaAgent(MultiAgentSearch):
    def __init__(self, agent_id):
        Agents.__init__(self, agent_id)
        self.max_depth = 3
