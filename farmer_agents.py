from agents import Agents
import random
from util import card_combinations


class ReflexAgent(Agents):
    def get_action(self, board):
        successors = self._hand.get_successors(board.previous_play, card_combinations)
        card_type, card_list, cards_left = random.choice(successors)
        self.refresh_hand(cards_left)
        return card_type, card_list, len(cards_left)


class MiniMaxAgent(Agents):
    def get_action(self, board):
        successors = self._hand.get_successors(board.previous_play, card_combinations)
