import unittest
from carddeck import CardDeck

class TestCardDeck(unittest.TestCase):

    def setUp(self):
        self._deck = CardDeck('test user')


    def test_length_of_deck_is_52(self):
        expected = 52
        self.assertEqual(len(self._deck), expected)

    def test_invalid_name_raises_err(self):
        with self.assertRaises(TypeError):
            d = CardDeck(1234)

    def test_drawing_card_reduces_len_by_one(self):
        expected = 51
        self._deck.draw()
        self.assertEqual(len(self._deck), expected)

if __name__ == '__main__':
    unittest.main()

