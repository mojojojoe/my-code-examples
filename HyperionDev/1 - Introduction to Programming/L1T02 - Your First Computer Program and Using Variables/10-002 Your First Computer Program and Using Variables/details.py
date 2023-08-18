#!/bin/env python3
""" 
Applied a script template where python looks to see whether the file is the 'main' file and if it is the script in the subsequent function call is listed.
The run_it script that is run takes four inputs and places the inputs gained from the differing prompt messages into four variables.
A template string is assigned to a variable laying out a letter using the above variables using the f string format.
Finally the string is printed to standard output. 

 """

from datetime import datetime

def run_it()->int:
    name = input("Please type in your name: ")
    age = input(f"\nThanks {name},  now please type in your age: ")
    street = input(f"\n {name}, can you tell me where you live? (the street name)")
    street_num = input("\nThanks, and finally, can you please tell me the street number? ")
    letter = f"""
                            {street_num} {street} Street
                            {datetime.now():%d %B %Y.}                  
                    
    Dear {name},
    
        We wish you a happy hundred now that you have reached the {age} milestone.
        
    Kind regards,
    The Team                                  
    """    
    
    print("Here is a letter:\n")
    print(letter)
    
    
if __name__ == '__main__':
    run_it()
