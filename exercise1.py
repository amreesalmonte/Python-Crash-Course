number = 5 #int
guess = input("Guess a number: ")

print(type(guess)) #printing the data type of guess

#executes code depending on the expression
if number == int(guess):
  print("Congrats, you guessed correctly")
else:
  print("Wrong guess")
