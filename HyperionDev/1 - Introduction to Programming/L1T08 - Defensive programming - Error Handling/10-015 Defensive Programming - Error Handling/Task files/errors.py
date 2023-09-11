# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # syntax error: missing parentheses
print ("\n") # syntax error: missing parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # style misuse: mixing camel toe and snake naming in variable naming . 
# runtime error: '==' is not an assignment but a logical operator
age = float(age_str) # runtime error: age_str was not castable as there are alphabetic characters in the string 
print(f"I\'m {age_str} years old.") # syntax error: the apostrophe needed an escape slash. f string formulation made.  

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # logical error: years from now is declared as a string but in the next statement will undergo numeric operation 
# leading to an undesired effect. I removed the quotation marks to declare it as a float. NB creating a float makes it 
# better to cast the age as a float too. 3 was changed to 3.5 to fit the last print function which highlighted 3 years 
# and six months.
total_years = age + years_from_now # style: perhaps better choice for variable  naming can be made.
# syntax error: lines 8 to 15 were improperly indented
print (f"The total number of years: {total_years}") # syntax error: print function not parenthesised, also the variable total_years was incorrectly called answer_years. 
# answer_years was also quoted. The string was changed to f-string format.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = int(total_years * 12) # logical error: had to be cast to int so that total_months wouldn't print a float.
print (f"In 3 years and 6 months, I'll be {total_months} months old") # syntax error: print function not parenthesised. f string was created for convenience. And string reformulated.

#HINT, 330 months is the correct answer

