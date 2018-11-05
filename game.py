from board import Board
from farmer_agents import FarmerAgents
from landlord_agents import LandlordAgents
from util import CardCombinations
from constants import FARMER_ONE, FARMER_TWO, LANDLORD


class FightingWithLandlordGame(object):
    def __init__(self):
        self._board = Board()

    def setup(self):
        print('Shuffle and dealing cards...')
        pile1, pile2, pile3 = self._board.deal()
        landlord_hand = pile1 + self._board.base_card

        landlord = LandlordAgents(landlord_hand)
        farmer_one = FarmerAgents(pile2)
        farmer_two = FarmerAgents(pile3)
        cb = CardCombinations()
        cb.get_all_combinations()

    def start_game(self):

        pass
