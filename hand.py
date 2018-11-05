from collections import Counter

class Hand(object):
    def __init__(self, card_list):
        self._card_list = sorted(card_list)
        self._single = []
        self._pair = []
        self._trio = []
        self._bomb = []
        self._king_bomb = []
        self._chain = []
        self._is_pass = False
        self._counter = Counter(card_list)


    def get_successors(self, card_list):
        #todo
        pass
