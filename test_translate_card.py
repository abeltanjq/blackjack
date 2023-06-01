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

    def test_for_hearts(self):
        for i in range(2,10):
            self.assertEqual(f"{i}♡", translate_card(deck_of_cards.Card((1,i))))
        
        self.assertEqual("A♡", translate_card(deck_of_cards.Card((1,1))))
        self.assertEqual("J♡", translate_card(deck_of_cards.Card((1,11))))
        self.assertEqual("Q♡", translate_card(deck_of_cards.Card((1,12))))
        self.assertEqual("K♡", translate_card(deck_of_cards.Card((1,13))))
    
    def test_for_diamonds(self):
        for i in range(2,10):
            self.assertEqual(f"{i}♢", translate_card(deck_of_cards.Card((2,i))))
        
        self.assertEqual("A♢", translate_card(deck_of_cards.Card((2,1))))
        self.assertEqual("J♢", translate_card(deck_of_cards.Card((2,11))))
        self.assertEqual("Q♢", translate_card(deck_of_cards.Card((2,12))))
        self.assertEqual("K♢", translate_card(deck_of_cards.Card((2,13))))
    
    def test_for_clubs(self):
        for i in range(2,10):
            self.assertEqual(f"{i}♣", translate_card(deck_of_cards.Card((3,i))))
        
        self.assertEqual("A♣", translate_card(deck_of_cards.Card((3,1))))
        self.assertEqual("J♣", translate_card(deck_of_cards.Card((3,11))))
        self.assertEqual("Q♣", translate_card(deck_of_cards.Card((3,12))))
        self.assertEqual("K♣", translate_card(deck_of_cards.Card((3,13))))

if __name__ == '__main__':
    unittest.main()
