from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call parent method
        for j in 1, 2:
            joker = 'Joker', j
            self._cards.append(joker)
