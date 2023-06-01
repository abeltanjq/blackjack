def input_bet(deposit):
    bet = input("Your bet: ")
    if bet.isdigit() and (0 < int(bet) < deposit):
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


def main():
    print("Hi! Please put in your initial deposit (min 1 credit).")
    deposit = input_deposit()
    bet = input_bet(deposit)

if __name__ == '__main__':
    main()
