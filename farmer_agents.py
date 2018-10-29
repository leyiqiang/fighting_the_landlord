from agents import Agents
from hand import Hand


class FarmerAgents(Agents):
    def __init__(self, position):
        Agents.__init__(self, position)
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card_list):
        self.hand.card_list = card_list
