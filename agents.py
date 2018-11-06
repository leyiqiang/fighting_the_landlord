from hand import Hand
import pprint
from util import raise_not_defined


class Agents:
    def __init__(self, card_list):
        self._hand = Hand(card_list)

    # def get_successors(self, board):
    #     print(self._hand.card_list)
    #     successors = self._hand.get_successors(board.previous_play, board.card_combinations)
    #     pp = pprint.PrettyPrinter()
    #     pp.pprint(successors)

    def refresh_hand(self, new_list):
        self._hand = Hand(new_list)

    def get_action(self, board):
        raise_not_defined()


class ManualAgent(Agents):
    def __init__(self, card_list):
        Agents.__init__(self, card_list)

    def get_action(self, board):
        pass

