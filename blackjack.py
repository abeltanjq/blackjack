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

if __name__ == '__main__':
    main()
