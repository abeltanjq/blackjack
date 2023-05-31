def input_deposit():
    deposit = input("Initial Deposit: ")
    return deposit


def main():
    print("Hi! Please put in your initial deposit (min 1 credit).")
    deposit = input_deposit()

if __name__ == '__main__':
    main()
