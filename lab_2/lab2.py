# If continuing the program, ask for input for num_element in range
while True: 
    #Request input from user and store as num_elements
    num_elements = input("Enter your value: ")
    print(num_elements)

    #Create counter variables called num_fizz, num_buzz, num_fizz_buzz that keep track of how many times each was printed
    num_fizz=0;
    num_buzz=0;
    fizz_buzz=0;

    #Create for loop spanning until num_elements
    for x in range (int(num_elements)):
        #In each iteration of the for loop print an f-string saying the iteration number
        print(x)
        #If the iteration number is divisible by 3 print “Fizz”
        result_three = x % 3
        if result_three == 0:
            print ('Fizz')
            num_fizz+=1
        #If the iteration number is divisible by 5 print "Buzz"
        result_five = x % 5
        if result_five == 0:
            print ('Buzz')
            num_buzz+=1
        #If the iteration number is divisible by 3 and 5 print “FizzBuzz”
        if result_five == 0 and result_three == 0:
            print ('FizzBuzz')
            fizz_buzz+=1
    # After completing loop over range inputted by user print number of occurences of fizz, buzz, and fizz buzzCreate counter variables called num_fizz, num_buzz, num_fizz_buzz that keep track of how many times each was printed
    print(f"Fizz: ({num_fizz})")
    print(f"Buzz: ({num_buzz})")
    print(f"Fuzz_Buzz: ({fizz_buzz})")

#Ask the user if they would like to exit the program, exit if yes
    continue_loop = input("Would you like to exit? (y/n)")
    if(continue_loop.lower()=="y"):
        print("Exiting program...")
        break 
    
