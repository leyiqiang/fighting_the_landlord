from board import Board
from farmer_agents import FarmerAgents
from landlord_agents import LandlordAgents
from constants import FARMER_ONE, FARMER_TWO, LANDLORD


class FightingWithLandlordGame(object):
    def __init__(self):
        self.board = Board()

    def setup(self):
        print('Shuffle and dealing cards...')
        pile1, pile2, pile3 = self.board.deal()
        landlord_hand = pile1 + self.board.base_card

        landlord = LandlordAgents(landlord_hand)
        farmer_one = FarmerAgents(pile2)
        farmer_two = FarmerAgents(pile3)
        # successors = farmer_two._hand.get_successors(self.board)
        # print(successors)

    def start_game(self):
        pass
