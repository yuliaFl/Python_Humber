# Print hello to Humber bank terminal and ask user for input for 4-digit pin
print('Hello to Humber Banking')

correct_pin = '2895'
attempts = 3
balance = 29583.78  

# Use functions for each bank operation
# All dollar amounts will be displayed with 2 decimal places
# All operations will be checked for valid input before proceeding

# Entering 1 will display the balance
def display_balance(balance):
    print(f'Your current balance is ${balance:.2f}')
# Entering 2 will allow making a withdrawal

# Entering 3 will allow making a deposit
# When depositing will directly ask how much user wants to deposit and show updated amount once user enters it
def make_deposit(balance):
    deposit_amount = float(input("How much would you like to deposit: "))
    balance = balance + deposit_amount
    print(f"New balance: ${balance:.2f}")

# After each operation user is asked if they would like to perform another action
# When making a withdrawal user is presented default options as well as custom
# After user selects option (20, 40, 60, 80, 100) or enters custom it will be deducted from balance. 
# Display new balance immediately
# Ensure user has enough money before withdrawal
def make_withdraw(balance):
    print("Choose option to withdraw")
    print("1. $20\n2. $40\n3. $60\n4. $80\n5. $100\n6. Custom")
    choice = input("Select an option for withdrawal: ")
        

# User has 3 chances to enter the correct pin otherwise program exits

while attempts > 0:
    user_pin = input('Please enter your 4-digit PIN: ')

    if user_pin == correct_pin:
        # When the correct PIN is entered, the user is given the main menu
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
            # Entering 4 will exit the program
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again")

            continue_choice = input("Would you like to continue? (y/n): ")
            if continue_choice != 'y':
                break

    else:
        print('Incorrect PIN.')
        attempts -= 1

    break

if attempts == 0:
    print('You have run out of attempts. Exiting.')


    # break loop (should not break out after incorect pin, but need to break out when 'n')