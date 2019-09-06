class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit


class DeckOfCards:

    def __init__(self):
        self.cards = self.__initialize_deck__()

    def _initialize_deck__(self):
        pass

    def shuffle(self):
        pass

    def cut(self):
        pass
