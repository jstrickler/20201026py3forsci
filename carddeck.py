import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit


class CardDeck:  # inherit from object
    SUITS = 'clubs diamonds hearts spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property (read-only by default)
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self._cards)})"

    def __len__(self):
        return len(self._cards)
