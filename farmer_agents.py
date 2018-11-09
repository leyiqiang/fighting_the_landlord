from agents import Agents, MultiAgentSearch, ManualAgent
import random
from hand import Hand


class ReflexAgent(Agents):
    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        card_type, card_list = random.choice(actions)
        return card_type, card_list


class MiniMaxAgent(MultiAgentSearch):
    """
    A minimax agent will take very long time to finish, I will only implement the Alpha Beta pruning version
    """

    def __init__(self, agent_id):
        Agents.__init__(self, agent_id)
        self.max_depth = 2


class ManualTerminalAgent(ManualAgent):
    def __init__(self, agent_id):
        ManualAgent.__init__(self, agent_id)


class AlphaBetaAgent(MultiAgentSearch):

    def __init__(self, agent_id):
        Agents.__init__(self, agent_id)
        self.max_depth = 2

    # successors is a list of tuple (play_type, card_list)
    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        alpha = float('-inf')
        beta = float('+inf')
        max_val = float('-inf')
        next_action = None
        for a in actions:
            next_state = board_state.next_state(a)
            if next_state.get_position(next_state.turn) != 0:  # the farmer(max) turn
                val = self.get_max_value(0, next_state, alpha, beta)
            else:
                val = self.get_min_value(0, next_state, alpha, beta)
            if max_val < val:
                max_val = val
                next_action = a
            alpha = max(alpha, max_val)
        return next_action

    def get_min_value(self, current_depth, current_state, alpha, beta):
        min_val = float('+inf')
        actions = current_state.get_actions(current_state.turn)
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state)
        for a in actions:
            next_state = current_state.next_state(a)
            min_val = min(min_val, self.get_max_value(current_depth, next_state, alpha, beta))
            if min_val < alpha:
                return min_val
            beta = min(min_val, beta)
        return min_val

    def get_max_value(self, current_depth, current_state, alpha, beta):
        max_val = float('-inf')
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state)
        if current_state.get_position(current_state.turn) == 2:
            actions = current_state.get_actions(current_state.turn)
            for a in actions:
                next_state = current_state.next_state(a)
                max_val = max(max_val, self.get_min_value(current_depth, next_state, alpha, beta))
                if max_val > beta:
                    return max_val
                alpha = max(alpha, max_val)
            return max_val
        else:
            actions = current_state.get_actions(current_state.turn)
            for a in actions:
                next_state = current_state.next_state(a)
                max_val = max(max_val, self.get_max_value(current_depth + 1, next_state, alpha, beta))
                if max_val > beta:
                    return max_val
                alpha = max(alpha, max_val)
            return max_val
