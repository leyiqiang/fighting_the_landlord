from deck import Deck
from farmer_agents import FarmerAgents
from landlord_agents import LandlordAgents
import random
from constants import FARMER_ONE, FARMER_TWO, LANDLORD


class FightingWithLandlordGame(object):
    def __init__(self):
        self._agent_order = random.shuffle([FARMER_ONE, FARMER_TWO, LANDLORD])

    def start_game(self):
        # shuffle card
        print('Initializing players...')
        # randomly choose location
        landlord = LandlordAgents()
        farmer_one = FarmerAgents()
        farmer_two = FarmerAgents()
        print('Shuffle and dealing cards...')
        deck = Deck()
        pile1, pile2, pile3 = deck.deal()
        landlord.card_list = pile1 + deck.base_card
        farmer_one.card_list = pile2
        farmer_two.card_list = pile3
        print(deck.base_card)
