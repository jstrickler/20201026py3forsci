from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck() # call parent function
        j1 = '1', 'JOKER'
        j2 = '2', 'JOKER'
        self._cards.append(j1)
        self._cards.append(j2)


