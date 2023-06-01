import unittest
from blackjack import translate_card
from deck_of_cards import deck_of_cards

class TestTranslateCard(unittest.TestCase):

    def test_spades_from_2_to_10(self):
        for i in range(2,10):
            self.assertEqual(f"{i}♠", translate_card(deck_of_cards.Card((0,i))))

    def test_ace_of_spades(self):
        self.assertEqual("A♠", translate_card(deck_of_cards.Card((0,1))))

if __name__ == '__main__':
    unittest.main()
