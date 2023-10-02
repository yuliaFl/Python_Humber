# Import random module
import random
# Add counter variable to keep track of number of wins and total games
wins = 0
games = 0   

# Move code used to get user input for min/max and getting random number to its own function
def getParams():
# Ask user input to get min and max numbers for range
    min_value = int(input("Enter min value: "))
    max_value = int(input("Enter max value: "))  
    return min_value, max_value

# Move code used to determine if number is divisible by 3 and 5 to its own function
def divisible(guess_value):
    result_three = guess_value % 3
    result_five = guess_value % 5
    if result_three == 0:
        print("Fizz")
    if result_five == 0:
        print("Buzz")  

# Move code used to print win percent and ask if user wants to reset statistics to its own function
def resetStats():
    global wins  # Declare wins as a global variable
    percentage = wins / games
    print(f"Total percentage of wins {percentage:.2f}")
    reset_question = input("Would you like to reset statistics? (y/n): ")
    if reset_question.lower() == "y":
        wins = 0

wins = 0
games = 0

# If yes, ask user input for min and max number in range
while True:         
    # Ask user input to get min and max numbers for range
    min_value, max_value = getParams()
    # Generate a random number in range requested by user
    random_value = random.randint(min_value, max_value)
    # Ask user input to guess number
    guess_value = input("Enter guess number: ")
    # Determine if guessed number is the same as the random number
    if int(guess_value) == int(random_value): 
        # Print result to user
        print(f"You guessed it right {random_value}")
        wins+=1
        games+=1
    else:
        print(f"Wrong, the right number was {random_value}")
        games+=1
    # Ask user input if they would like to play again
    continue_loop = input("Would you like to play again? (y/n)")
    if(continue_loop.lower()=="n"):
        print("Exiting program...")
        break 
    resetStats()
    # Add the end of each round print number of games won, total number and percentage of games won formatted to 2 decimal places
    print(f"Total wins {wins}, Total games {games}")
