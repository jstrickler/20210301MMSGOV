import random

class Card:
   pass

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):  # constructor (initializer)
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []   # list of cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    @property
    def dealer(self):   # "getter" property
        return self._dealer  # return private data

    # dealer = property(dealer)

    @dealer.setter
    def dealer(self, dealer_name):   # "setter" property
        if isinstance(dealer_name, str):
            self._dealer = dealer_name
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if not self._cards:
            raise ValueError("Deck is empty")
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):  # human-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return "{} Dealer:{}, Cards Left:{}".format(my_name, self.dealer, len(self))

    def __repr__(self):  # interpreter-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return "{}('{}')".format(my_name, self.dealer)

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards += other._cards
        return tmp

