from deck import Deck
from farmer_agents import FarmerAgents
from landlord_agents import LandlordAgents
import random


class FightingWithLandlordGame(object):
    def __init__(self):
        # round
        #
        pass

    def start(self):
        # shuffle card
        # select one player as landlord
        print('Initializing players...')
        # randomly choose location
        agent_order = random.shuffle([0, 1, 2])
        landlord = LandlordAgents(agent_order.pop())
        agent_farmer1 = FarmerAgents(agent_order.pop())
        agent_farmer2 = FarmerAgents(agent_order.pop())
        print('Shuffle and dealing cards...')
        deck = Deck()
        deck.deal()
        pass
