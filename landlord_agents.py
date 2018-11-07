from agents import Agents
import random


class ReflexAgent(Agents):

    def get_action(self, board):
        successors = self._hand.get_successors(board.previous_play, board.card_combinations)
        card_type, card_list, cards_left = random.choice(successors)
        self.refresh_hand(cards_left)
        return card_type, card_list, len(cards_left)


class MiniMaxAgent(Agents):

    def get_action(self, board):
        pass