from board import Board
from input_parser import InputParser
import farmer_agents
import landlord_agents
from constants import FARMER_ONE, FARMER_TWO, LANDLORD
import random
import itertools


class FightingWithLandlordGame(object):
    def __init__(self):
        self.board = Board()
        self._landlord = None
        self._farmer_one = None
        self._farmer_two = None
        self._players = None

    def setup(self, parser):
        print('Order of the game:')
        print(self.board.agent_order_pretty)
        pile1, pile2, pile3 = self.board.deal()
        landlord_hand = pile1 + self.board.base_card
        # select player
        player = random.choice([FARMER_ONE, FARMER_TWO, LANDLORD])
        LandlordAgents = getattr(landlord_agents, parser.landlord_agent)
        FarmerAgents = getattr(farmer_agents, parser.farmer_agent)
        if player == FARMER_ONE:
            PlayerAgents = getattr(farmer_agents, parser.player_agent)
            print('You are farmer1!')
            self._landlord = LandlordAgents(landlord_hand)
            self._farmer_one = PlayerAgents(pile2)
            self._farmer_two = FarmerAgents(pile3)
        if player == FARMER_TWO:
            print('You are farmer2!')
            PlayerAgents = getattr(farmer_agents, parser.player_agent)
            self._landlord = LandlordAgents(landlord_hand)
            self._farmer_one = FarmerAgents(pile2)
            self._farmer_two = PlayerAgents(pile3)
        if player == LANDLORD:
            print('You are landlord!')
            PlayerAgents = getattr(landlord_agents, parser.player_agent)
            self._landlord = PlayerAgents(landlord_hand)
            self._farmer_one = FarmerAgents(pile2)
            self._farmer_two = FarmerAgents(pile3)
        print('***GAME START***')
        self.start_game()

    def start_game(self):
        for turn in itertools.cycle(self.board.agent_order):
            action = None
            if turn == FARMER_ONE:
                action = self._farmer_one.get_action(self.board)
            if turn == FARMER_TWO:
                action = self._farmer_two.get_action(self.board)
            if turn == LANDLORD:
                action = self._landlord.get_action(self.board)
            self.board.play(action, turn)


if __name__ == '__main__':
    parser = InputParser()
    parser.parse_input()
    game = FightingWithLandlordGame()
    game.setup(parser)
