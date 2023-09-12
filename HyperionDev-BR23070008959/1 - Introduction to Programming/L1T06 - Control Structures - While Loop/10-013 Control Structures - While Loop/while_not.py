import random # import tha random library that enables use of its built-in functions
num = random.randint(1,50) # use the radint (i.e. random integer) function from the random library to get a random integer between 1 and 50
num_guess = int(input("Guess a number from 1 to 50: "))

while num_guess != num:
    if num_guess < num:
        num_guess = int(input("Too small! Guess another number from 1 to 50: "))
    else:  num_guess = int(input("Too big! Guess another number from 1 to 50: "))
    
print("You guessed correctly!")
