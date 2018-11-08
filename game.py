from board import HandsFaceUpBoardData
from input_parser import InputParser
import farmer_agents
import landlord_agents
from constants import *
import random
import copy


class FightingWithLandlordGame(object):
    def __init__(self):
        self.board_state = HandsFaceUpBoardData()
        self._landlord = None
        self._farmer_one = None
        self._farmer_two = None
        self._players = None

    def setup(self, game_parser):
        print('Order of the game:')
        print(self.board_state.agent_order_pretty)
        # select player
        player = random.choice([FARMER_ONE, FARMER_TWO, LANDLORD])
        LandlordAgents = getattr(landlord_agents, game_parser.landlord_agent)
        FarmerAgents = getattr(farmer_agents, game_parser.farmer_agent)
        if player == FARMER_ONE:
            PlayerAgents = getattr(farmer_agents, game_parser.player_agent)
            print('You are farmer1!')
            self._landlord = LandlordAgents(LANDLORD)
            self._farmer_one = PlayerAgents(FARMER_ONE)
            self._farmer_two = FarmerAgents(FARMER_TWO)
        if player == FARMER_TWO:
            print('You are farmer2!')
            PlayerAgents = getattr(farmer_agents, game_parser.player_agent)
            self._landlord = LandlordAgents(LANDLORD)
            self._farmer_one = FarmerAgents(FARMER_ONE)
            self._farmer_two = PlayerAgents(FARMER_TWO)
        if player == LANDLORD or True:
            print('You are landlord!')
            PlayerAgents = getattr(landlord_agents, game_parser.player_agent)
            self._landlord = PlayerAgents(LANDLORD)
            self._farmer_one = FarmerAgents(FARMER_ONE)
            self._farmer_two = FarmerAgents(FARMER_TWO)
        print('landlord hand:{}'.format(sorted(self.board_state.hands[LANDLORD])))
        print('farmer1 hand:{}'.format(sorted(self.board_state.hands[FARMER_ONE])))
        print('farmer2 hand:{}'.format(sorted(self.board_state.hands[FARMER_TWO])))

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
        print('*** GAME OVER, {0} WIN ***'.format(self.board_state.winner))


if __name__ == '__main__':
    parser = InputParser()
    parser.parse_input()
    game = FightingWithLandlordGame()
    game.setup(parser)
    game.start_game()
