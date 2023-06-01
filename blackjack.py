from deck_of_cards import deck_of_cards

def input_bet(deposit):
    bet = input("Your bet: ")
    if bet.isdigit() and (0 < int(bet) <= deposit):
        return int(bet)
        
    print("Bet has to be an integer between 0 and your deposit amount")
    return input_bet(deposit)

def input_deposit():
    deposit = input("Initial Deposit: ")

    if not deposit.isdigit():
        print("Deposit has to be a number >= 1 and no decimals.")
        return input_deposit()
    else:
        return int(deposit)
    
def translate_card(card):
    suits = ['♠', '♡', '♢', '♣']
    specials = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }
    translated_rank = specials.get(card.rank) if specials.get(card.rank) else card.rank
    
    return f"{translated_rank}{suits[card.suit]}"


def main():
    print("Hi! Please put in your initial deposit (min 1 credit).")
    deposit = input_deposit()
    bet = input_bet(deposit)
    cards = deck_of_cards.DeckOfCards()
    cards.shuffle_deck()

    # Start game
    player = [cards.give_first_card(), cards.give_first_card()]
    print(f"Your hand: {translate_card(player[0])} {translate_card(player[1])}")

if __name__ == '__main__':
    main()
