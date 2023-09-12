# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # runtime error: this assignment was to an unquoted string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It has {number_of_teeth} teeth of a {animal_type}." #style: incorrect English use, 
# syntax error: f had to be prepended to the string to make it an f-string.

print (full_spec) # syntax error: wasn't parenthesised

