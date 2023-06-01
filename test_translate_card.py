import unittest
from blackjack import translate_card
from deck_of_cards import deck_of_cards

class TestTranslateCard(unittest.TestCase):
    
    def test_spades_from_2_to_10(self):
        for i in range(1,10):
            self.assertEqual(f"{i}♠", translate_card(deck_of_cards.Card((0,i))))

if __name__ == '__main__':
    unittest.main()
