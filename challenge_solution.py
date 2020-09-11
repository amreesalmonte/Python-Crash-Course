'''
Create a calculator that prompts the user to enter 2 numbers and add or subtract those numbers depending on the user input. Only end the program if the user chooses to. Try using functions when you answer this. If you need any help ask any of our tutors in the slack!
Flow of the program:
1. Ask the user to enter 2 numbers.
2. Ask the user if they want to add, subtract, or exit the program.
3. Execute the appropriate code depending on user input.
'''

def add_numbers(x, y):
    #function that prints the sum of 2 numbers
    print(x + y)

def sub_numbers(x, y):
    #function that prints the difference of 2 numbers
    print(x - y)

calculating = True #bool
while calculating: #keep executing code if calculating == True
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    #converted numbers to float instead because we want to be able to add and subtract numbers with decimals too
    operation = input("Type in add/sub/exit: ").lower() #changed to lower case because we don't want to program to be case sensitive

    if operation == "add":
        add_numbers(num1, num2) #passing information to the function x = num1, y = num2
    elif operation == "sub":
        sub_numbers(num1, num2) #passing information to the function
    else:
        calculating = False #stop the while loop and end the program

print("Goodbye! :)")


