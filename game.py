from board import GameBoardData
from input_parser import InputParser
import farmer_agents
import landlord_agents
from constants import *
import random


class FightingWithLandlordGame(object):
    def __init__(self):
        self.board_state = GameBoardData()
        self._landlord = None
        self._farmer_one = None
        self._farmer_two = None
        self._players = None

    def setup(self, game_parser):
        # todo: change --player to farmer2
        # todo: add evaluation functions
        print('Order of the game:')
        print(self.board_state.agent_order_pretty)
        # select player
        # player = random.choice([FARMER_ONE, FARMER_TWO, LANDLORD])
        LandlordAgents = getattr(landlord_agents, game_parser.landlord_agent)
        FarmerAgents = getattr(farmer_agents, game_parser.farmer_agent)
        evaluation = game_parser.evaluation
        rollout_policy = game_parser.rollout_policy
        # if player == FARMER_ONE:
        #     PlayerAgents = getattr(farmer_agents, game_parser.farmer_two_agent)
        #     print('You are farmer1!')
        #     self._landlord = LandlordAgents(LANDLORD, evaluation)
        #     self._farmer_one = PlayerAgents(FARMER_ONE, evaluation)
        #     self._farmer_two = FarmerAgents(FARMER_TWO, evaluation)
        # if player == FARMER_TWO:
        #     print('You are farmer2!')
        #     PlayerAgents = getattr(farmer_agents, game_parser.farmer_two_agent)
        #     self._landlord = LandlordAgents(LANDLORD, evaluation)
        #     self._farmer_one = FarmerAgents(FARMER_ONE, evaluation)
        #     self._farmer_two = PlayerAgents(FARMER_TWO, evaluation)
        # if player == LANDLORD:
        #     print('You are landlord!')
        # PlayerAgents = getattr(landlord_agents, game_parser.farmer_two_agent)
        self._landlord = LandlordAgents(LANDLORD, evaluation)
        self._farmer_one = FarmerAgents(FARMER_ONE, evaluation)
        self._farmer_two = FarmerAgents(FARMER_TWO, evaluation)
        print('landlord hand:{}'.format(sorted(self.board_state.get_hands(LANDLORD))))
        print('farmer1 hand:{}'.format(sorted(self.board_state.get_hands(FARMER_ONE))))
        print('farmer2 hand:{}'.format(sorted(self.board_state.get_hands(FARMER_TWO))))

    def start_game(self):
        print('***GAME START***')
        while not self.board_state.is_terminal:
            turn = self.board_state.turn
            action = None
            if turn == FARMER_ONE:
                action = self._farmer_one.get_action(self.board_state)
                print('farmer1 plays {0}'.format(action))
            if turn == FARMER_TWO:
                action = self._farmer_two.get_action(self.board_state)
                print('farmer2 plays {0}'.format(action))
            if turn == LANDLORD:
                action = self._landlord.get_action(self.board_state)
                print('landlord plays {0}'.format(action))
            self.board_state = self.board_state.next_state(action)
            # print('hands left landlord: {0}'.format(sorted(self.board_state.hands[LANDLORD])))
            # print('hands left farmer one: {0}'.format(sorted(self.board_state.hands[FARMER_ONE])))
            # print('hands left farmer two: {0}'.format(sorted(self.board_state.hands[FARMER_TWO])))
        print('*** GAME OVER, {0} WIN ***'.format(self.board_state.winner))


if __name__ == '__main__':
    parser = InputParser()
    parser.parse_input()
    game = FightingWithLandlordGame()
    game.setup(parser)
    game.start_game()
