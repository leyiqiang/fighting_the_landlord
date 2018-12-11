import time

from agents import Agents, MultiAgentSearch, ManualAgent
import random
import math

from constants import RANDOM, LONGEST_COMBO, EVALUATION, CARD_VALUE, card_rating


class ReflexAgent(Agents):

    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        card_type, card_list = random.choice(actions)
        return card_type, card_list


class ManualTerminalAgent(ManualAgent):
    def __init__(self, agent_id):
        ManualAgent.__init__(self, agent_id)


class MiniMaxAgent(MultiAgentSearch):
    """
    A minimax agent will take really long time to calculate
    """
    def __init__(self, agent_id, evaluation):
        Agents.__init__(self, agent_id, evaluation)
        self.max_depth = 2

    # successors is a list of tuple (play_type, card_list)
    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        max_val = float('-inf')
        next_action = None
        for a in actions:
            next_state = board_state.next_state(a)
            min_val = self.get_min_value(0, next_state)
            if min_val > max_val:
                max_val = min_val
                next_action = a
        return next_action

    def get_min_value(self, current_depth, current_state):
        actions = current_state.get_actions(current_state.turn)
        values = []
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state)
        if current_state.get_position(current_state.turn) == 2:  # last min, return to landlord
            for a in actions:
                next_state = current_state.next_state(a)
                values.append(self.get_max_value(current_depth + 1, next_state))
            return min(values)
        else:  # next player is still farmer, get min
            for a in actions:
                next_state = current_state.next_state(a)
                values.append(self.get_min_value(current_depth, next_state))
            return min(values)

    def get_max_value(self, current_depth, current_state):
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state)
        else:
            actions = current_state.get_actions(self.agent_id)
            values = []
            for a in actions:
                next_state = current_state.next_state(a)
                values.append(self.get_min_value(current_depth + 1, next_state))
            return max(values)


class AlphaBetaAgent(MultiAgentSearch):

    def __init__(self, agent_id, evaluation, depth=2):
        Agents.__init__(self, agent_id, evaluation)
        self.max_depth = depth

    # successors is a list of tuple (play_type, card_list)
    def get_action(self, board_state):
        actions = board_state.get_actions(self.agent_id)
        alpha = float('-inf')
        beta = float('+inf')
        max_val = float('-inf')
        next_action = None
        for a in actions:
            next_state = board_state.next_state(a)
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
            return self.evaluate(current_state, self.evaluation)
        if current_state.get_position(current_state.turn) == 2:  # last min, return to landlord
            for a in actions:
                next_state = current_state.next_state(a)
                min_val = min(min_val, self.get_max_value(current_depth + 1, next_state, alpha, beta))
                if min_val < alpha:
                    return min_val
                beta = min(min_val, beta)
            return min_val
        else:  # next player is still farmer, get min
            for a in actions:
                next_state = current_state.next_state(a)
                min_val = min(min_val, self.get_min_value(current_depth, next_state, alpha, beta))
                if min_val < alpha:
                    return min_val
                beta = min(min_val, beta)
            return min_val

    def get_max_value(self, current_depth, current_state, alpha, beta):
        max_val = float('-inf')
        if self.is_terminal(current_depth, current_state):
            return self.evaluate(current_state, self.evaluation)
        else:
            actions = current_state.get_actions(current_state.turn)
            for a in actions:
                next_state = current_state.next_state(a)
                max_val = max(max_val, self.get_min_value(current_depth, next_state, alpha, beta))
                if max_val > beta:
                    return max_val
                alpha = max(alpha, max_val)
            return max_val


class MCTAgent(Agents):
    def __init__(self, agent_id, evaluation):
        Agents.__init__(self, agent_id, evaluation)
        self.wins = {}  # a (agent_id, state): count dict
        self.plays = {}  # a (agent_id, state): count dict
        self.depth = 60
        self.simulation_time = 10
        # self.board_states = []

    def get_action(self, board):
        iteration = 0
        actions = board.get_actions(self.agent_id)

        timeout = time.time() + self.simulation_time
        while time.time() < timeout:
            iteration += 1
            parent_states = set()
            selected_state = self.select_state(board, parent_states)
            if selected_state.is_terminal:
                if selected_state.winner == self.agent_id:
                    reward = 1
                else:
                    reward = 0
            else:
                reward = self.rollout(selected_state)
            self.back_propagation(parent_states, reward)

        possible_moves = []
        for a in actions:
            next_state = board.next_state(a)
            possible_moves.append((next_state, a))
        win_rate, action = max(
            (self.wins.get(state.formalize(self.agent_id), 0) / self.plays.get(state.formalize(self.agent_id), 1), a)
            for state, a in possible_moves
        )
        print('win rate:{0}'.format(win_rate))
        return action

    def formalize_state(self, state):
        return state.formalize(self.agent_id)

    def select_state(self, board_state, parent_states):
        actions = board_state.get_actions()
        next_states = [board_state.next_state(a) for a in actions]
        if len(next_states) == 0:
            return board_state
        # if fully expanded, use UCB1 algorithm to select deterministic branches
        unvisited_states = [s for s in next_states if s.formalize(self.agent_id) not in self.plays.keys()]
        visited_states = [s for s in next_states if s.formalize(self.agent_id) in self.plays.keys()]
        if len(visited_states) <= 0:
            return self.random_select(parent_states, unvisited_states)
        if len(unvisited_states) <= 0 or random.uniform(0, 1) < 0.5:  # too many options, need to force exploitation
            next_node = self.ucb1_select(visited_states)
            parent_states.add(next_node.formalize(self.agent_id))
            return self.select_state(next_node, parent_states)
        else:
            return self.random_select(parent_states, unvisited_states)

    def random_select(self, parent_states, states_list):
        unvisited_state = random.choice(states_list)
        formalized_unvisited_state = unvisited_state.formalize(self.agent_id)
        parent_states.add(formalized_unvisited_state)
        self.plays[formalized_unvisited_state] = 0
        self.wins[formalized_unvisited_state] = 0
        return unvisited_state

    def ucb1_select(self, states_list):
        # nj = sum([self.plays[s] for s in states_list])
        total_play = sum([self.plays[s.formalize(self.agent_id)] for s in states_list])
        log_total = math.log(total_play)
        max_score = -1
        max_state = states_list[0]
        for s in states_list:
            formalized_state = s.formalize(self.agent_id)
            score = (self.wins[formalized_state] / self.plays[formalized_state]) + \
                     2 * math.sqrt(log_total / self.plays[formalized_state])
            if score > max_score:
                max_score = score
                max_state = s
        return max_state

    def rollout(self, selected_state):
        for i in range(0, self.depth):
            action_list = selected_state.get_actions()
            if len(action_list) == 0:
                print(action_list)

            selected_state = self.rollout_policy(selected_state, action_list, self.evaluation)
            if selected_state.is_terminal:
                if selected_state.winner == self.agent_id:
                    return 1
                else:
                    return 0
        return 0

    def rollout_policy(self, select_node, action_list, roll_out_policy=RANDOM):
        # TODO use different heuristic
        action = random.choice(action_list)
        if roll_out_policy == RANDOM:
            action = random.choice(action_list)
        if roll_out_policy == LONGEST_COMBO:
            action = max(len(a[1]) for a in action_list)
        if roll_out_policy == CARD_VALUE:
            max_score = float('-inf')
            for a in action_list:
                type, hand = a
                total_ratings = sum(card_rating[c] for c in hand)
                if max_score < total_ratings:
                    max_score = total_ratings
                    action = a
        if roll_out_policy == EVALUATION:
            pass
        return select_node.next_state(action)

    def back_propagation(self, visited_node, reward):
        for state in visited_node:
            # print(visited_node)
            if state in self.plays:
                # print('here')
                self.plays[state] += 1
                self.wins[state] += reward

