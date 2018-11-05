from hand import Hand


class Agents(object):
    def __init__(self, card_list):
        self._hand = Hand(card_list)

    def get_successors(self, board):
        print(self._hand.card_list)
        successors = self._hand.get_successors(board)
        print(successors)