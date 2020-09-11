numbers_list = [1, 3, 4, 5, 4, 6, 5, 5] #list of ints
guess = int(input("Enter a number: "))

count = 0 #will be used to count how many times a number occurs in a list

#for loop going through every element in the list
for number in numbers_list:
  if number == guess:
    #count = count + 1 
    count += 1 #another way of sayin count = count + 1

print("Occurs " + str(count) + " times")