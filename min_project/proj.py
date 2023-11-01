print('Welcome to Humber Banking')

correct_pin = '2895'
attempts = 3
balance = 29583.78  

def display_balance(balance):
    print(f'Your current balance is ${balance:.2f}')

def make_withdraw(balance):
    print("Choose option to withdraw")
    print("1. $20\n2. $40\n3. $60\n4. $80\n5. $100\n6. Custom")
    choice = input("Select an option for withdrawal: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 5:
            withdraw_amount = [20, 40, 60, 80, 100][choice - 1]
            if balance >= withdraw_amount:
                balance -= withdraw_amount
                print(f"New balance: ${balance:.2f}")
            else:
                print("Not enough funds.")
        elif choice == 6:
            custom_amount = float(input("Enter a custom amount: "))
            if balance >= custom_amount:
                balance -= custom_amount
                print(f"New balance: ${balance:.2f}")
            else:
                print("Not enough funds.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid input. Try again")

def make_deposit(balance):
    deposit_amount = float(input("How much would you like to deposit: "))
    balance += deposit_amount
    print(f"New balance: ${balance:.2f}")

while attempts > 0:
    user_pin = input('Please enter your 4-digit PIN: ')

    if user_pin == correct_pin:
        while True:
            print("=========================")
            print("Main menu")
            print("1. Display the balance")
            print("2. Make a withdrawal")
            print("3. Make a deposit")
            print("4. Exit")
            print("=========================")

            choice = input("Choose one: ")

            if choice == '1':
                display_balance(balance)
            elif choice == '2':
                make_withdraw(balance)
            elif choice == '3':
                make_deposit(balance)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again")

            continue_choice = input("Would you like to continue? (y/n): ")
            if continue_choice.lower() != 'y':
                break

    else:
        print('Incorrect PIN.')
        attempts -= 1

if attempts == 0:
    print('You have run out of attempts. Exiting.')

