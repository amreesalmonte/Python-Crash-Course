letter = "a" #str

#will keep asking the user to guess until they get it correctly
playing = True #bool
while playing == True: 
  guess = input("Guess a letter: ")
  guess = guess.lower() #using a method to make the string lowercase
  if letter == guess:
    print("You guessed correctly")
    playing = False #this will stop the while loop
  else:
    print("Try Again")

print("Game Over")