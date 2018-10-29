from agents import Agents
from hand import Hand


class FarmerAgents(Agents):
    def __init__(self):
        Agents.__init__(self)
        self._hand = Hand()

