print("Welcome to ATM")

pin = input("Set your 4-digit PIN: ")

while len(pin) != 4 or not pin.isdigit():
    print("PIN must contain exactly 4 digits")
    pin = input("Set your 4-digit PIN: ")

balance = 1000

while True:
    enter_pin = input("Enter your PIN: ")

    if enter_pin == pin:
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Balance =", balance)

            elif choice == "2":
                amount = int(input("Enter amount: "))
                if amount > 0:
                    balance += amount
                    print("Deposit successful!")
                    print("New balance =", balance)
                else:
                    print("Enter a valid amount")

            elif choice == "3":
                amount = int(input("Enter amount: "))
                if amount <= 0:
                    print("Enter a valid amount")
                elif amount <= balance:
                    balance -= amount
                    print("Withdrawal successful!")
                    print("New balance =", balance)
                else:
                    print("Insufficient balance")

            elif choice == "4":
                print("Thank you for using ATM!")
                exit()

            else:
                print("Invalid choice")

    else:
        print("Wrong PIN")