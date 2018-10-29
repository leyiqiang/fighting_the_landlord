class Hand(object):
    # track current player's hand
    # get possible combinations
    # get successors based on previous turn(in ROUND)
    # play cards
    def __init__(self):
        self._card_list = []

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, card_list):
        self._card_list = card_list