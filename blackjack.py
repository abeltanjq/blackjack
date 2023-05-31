def input_deposit():
    deposit = input("Initial Deposit: ")
    if not deposit.isdigit():
        print("Deposit has to be an integer.")
        return input_deposit()
    
    if float(deposit) >= 1.0:
        return float(deposit)
    else:
        print("Initial deposit has to be >= 1).")
        return input_deposit()


def main():
    print("Hi! Please put in your initial deposit (min 1 credit).")
    deposit = input_deposit()

main()
