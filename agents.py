from hand import Hand
from util import raise_not_defined
from constants import card_rating, RANDOM, LONGEST_COMBO, EVALUATION, CARD_VALUE


class Agents:
    def __init__(self, agent_id, evaluation=RANDOM):
        self.agent_id = agent_id
        self.evaluation = evaluation
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

    def evaluate(self, board, evaluation):
        if board.is_win(self.agent_id):
            return 1000
        if board.is_loose(self.agent_id):
            return -1000
        # return 20 - len(board.get_hands(board.turn))
        hand = board.get_hands(self.agent_id)
        if evaluation == EVALUATION:
            return sum(card_rating[c] for c in hand) + 20 - len(hand)
        elif evaluation == CARD_VALUE:
            return sum(card_rating[c] for c in hand)
        # evaluation == MAX length
        else:
            return 20 - len(hand)

    def is_terminal(self, depth, board):
        return board.is_terminal or depth >= self.max_depth


class ManualAgent(Agents):
    def __init__(self, card_list, evaluation):
        Agents.__init__(self, card_list, evaluation)

    def get_action(self, board):
        while True:
            print('Your hand:')
            sorted_hand = sorted(board.get_hands(board.turn))
            # sorted_hand_pretty = [card_pretty_name[name] for name in sorted_hand]
            print(sorted_hand)
            result = input('What are you going to play?\n')
            try:
                card_list = result.split(',')
                if card_list[0] == 'PASS':
                    combo_type = 'PASS'
                    play = ()
                    return combo_type, play
                else:
                    card_list_int = list(map(int, card_list))
                    play = tuple(card_list_int)
                    action = Hand.get_combo_type(board.previous_play, play, board.combos[self.agent_id])
                return action
            except Exception as e:
                print('Invalid input or play, please try again.')

