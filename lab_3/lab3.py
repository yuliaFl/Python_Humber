# If yes, ask user input for min and max number in range
while True: 
    # Import random module
    import random 
    # Ask user input to get min and max numbers for range
    min_value = input("Enter min value: ")
    wins=+1
    games=+1
    max_value = input("Enter max value: ")
    # Generate a random number in range requested by user
    random_value = random.randint(int(min_value), int(max_value))
    # Ask user input to guess number
    guess_value = input("Enter guess number: ")
    # Determine if guessed number is the same as the random number
    if guess_value == random_value: 
    # Print result to user
        print(f"You guessed it right {random_value}")
    else:
        print(f"Wrong, the right number was {random_value}")
    # Ask user input if they would like to play again
    continue_loop = input("Would you like to play again? (y/n)")
    if(continue_loop.lower()=="n"):
        print("Exiting program...")
        break 
    print(f"Total wins {wins}, Total games {games}")
    # Add counter variable to keep track of number of wins and total games
    wins = 0
    games = 0 
    # Add the end of each round print number of games won, total number and percentage of games won formatted to 2 decimal places
    # At the end of each round ask if user would like to reset win/loss statistics
    # Move code used to get user input for min/max and getting random number to its own function
    # Move code used to determine if number is divisible by 3 and 5 to its own function
    # Move code used to print win percent and ask if user wants to reset statistics to its own function
