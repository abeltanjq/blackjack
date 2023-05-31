def input_deposit():
    deposit = input("Initial Deposit: ")

    if not deposit.isdigit():
        print("Deposit has to be a number >= 1.")
        return input_deposit()
    else:
        return float(deposit)


def main():
    print("Hi! Please put in your initial deposit (min 1 credit).")
    deposit = input_deposit()

if __name__ == '__main__':
    main()
