balance = 1700

while True:
    print("\n===== MONEY WITHDRAWAL SYSTEM =====")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount.")

            elif amount > balance:
                print("Error: Insufficient funds.")

                while True:
                    print("\nWhat would you like to do?")
                    print("1. Exit program")
                    print("2. Check current balance")
                    print("3. Re-enter withdrawal amount")

                    error_choice = input("Enter your choice (1/2/3): ")

                    if error_choice == "1":
                        print("Thank you for using the program.")
                        exit()

                    elif error_choice == "2":
                        print("Your current balance is:", balance)

                    elif error_choice == "3":
                        try:
                            new_amount = float(input("Enter new withdrawal amount: "))

                            if new_amount <= 0:
                                print("Please enter a valid amount.")

                            elif new_amount > balance:
                                print("Error: Insufficient funds again.")

                            else:
                                balance = balance - new_amount
                                print("Withdrawal successful!")
                                print("Remaining balance is:", balance)
                                break
                        except ValueError:
                            print("Invalid input. Please enter numbers only.")

                    else:
                        print("Invalid choice. Try again.")
            else:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Remaining balance is:", balance)

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        print("Your current balance is:", balance)

    elif choice == "3":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")