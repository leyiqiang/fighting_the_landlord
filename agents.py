from hand import Hand
import pprint
from util import raise_not_defined


class Agents:
    def __init__(self, agent_id):
        self.agent_id = agent_id
    # def get_successors(self, board):
    #     print(self._hand.card_list)
    #     successors = self._hand.get_successors(board.previous_play, board.card_combinations)
    #     pp = pprint.PrettyPrinter()
    #     pp.pprint(successors)

    def get_action(self, board):
        raise_not_defined()


class MultiAgentSearch(Agents):
    def __init__(self, agent_id, max_depth=10):
        Agents.__init__(self, agent_id)
        self.max_depth = max_depth

    def evaluate(self, board):
        if board.is_win(self.agent_id):
            return 1
        if board.is_loose(self.agent_id):
            return -1
        return 0

    def is_terminal(self, depth, board):
        # print(depth)
        # print(self.max_depth)
        return board.is_terminal or depth >= self.max_depth


class ManualAgent(Agents):
    def __init__(self, card_list):
        Agents.__init__(self, card_list)

    def get_action(self, board):
        pass

