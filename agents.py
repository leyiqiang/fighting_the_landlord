from hand import Hand


class Agents(object):
    def __init__(self):
        self.card_list = []
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card_list):
        self.hand.card_list = card_list
