from board import BoardData
from input_parser import InputParser
import farmer_agents
import landlord_agents
from constants import *
import random
import copy


class FightingWithLandlordGame(object):
    def __init__(self):
        self.board_state = BoardData()
        self._landlord = None
        self._farmer_one = None
        self._farmer_two = None
        self._players = None
        deck_without_joker = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, J, Q, K, A, TWO] * 4
        self._deck = deck_without_joker + [BLACK_JOKER, RED_JOKER]
        farmer_order = random.sample([FARMER_ONE, FARMER_TWO], 2)
        self._agent_order = [LANDLORD] + farmer_order

    def setup(self, parser):
        print('Order of the game:')
        print(self.board_state.agent_order_pretty)
        base_card, pile1, pile2, pile3 = self.deal()
        self.board_state.base_card = base_card
        landlord_hand = pile1 + base_card
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
        print('landlord hand:{}'.format(sorted(landlord_hand)))
        print('farmer1 hand:{}'.format(sorted(pile2)))
        print('farmer2 hand:{}'.format(sorted(pile3)))

    def deal(self):
        random.shuffle(self._deck)
        # create three public cards for landlord
        base_card = self._deck[0:3]
        # deal deck into 17 cards
        pile_one = self._deck[3: 20]
        pile_two = self._deck[20: 37]
        pile_three = self._deck[37: 54]
        return base_card, pile_one, pile_two, pile_three

    def start_game(self):
        print('***GAME START***')
        while not self.board_state.is_terminal:
            turn = self.board_state.current_turn
            action = None
            if turn == FARMER_ONE:
                action = self._farmer_one.get_action(self.board_state)
            if turn == FARMER_TWO:
                action = self._farmer_two.get_action(self.board_state)
            if turn == LANDLORD:
                action = self._landlord.get_action(self.board_state)
            print('{0} plays {1}'.format(self.board_state.current_turn, action))
            self.board_state = copy.deepcopy(self.board_state.next_state(action))
        print('*** GAME OVER, {0} WIN ***'.format(self.board_state.winner))


if __name__ == '__main__':
    parser = InputParser()
    parser.parse_input()
    game = FightingWithLandlordGame()
    game.setup(parser)
    game.start_game()
