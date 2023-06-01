import unittest
from blackjack import translate_card
from deck_of_cards import deck_of_cards

class TestTranslateCard(unittest.TestCase):

    def test_spades_from_2_to_10(self):
        for i in range(2,10):
            self.assertEqual(f"{i}♠", translate_card(deck_of_cards.Card((0,i))))

    def test_ace_of_spades(self):
        self.assertEqual("A♠", translate_card(deck_of_cards.Card((0,1))))

    def test_picture_of_spades(self):
        self.assertEqual("J♠", translate_card(deck_of_cards.Card((0,11))))
        self.assertEqual("Q♠", translate_card(deck_of_cards.Card((0,12))))
        self.assertEqual("K♠", translate_card(deck_of_cards.Card((0,13))))

if __name__ == '__main__':
    unittest.main()
