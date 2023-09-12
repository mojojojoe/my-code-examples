#!/usr/bin/env python3
"""
Ask for the user name.
Perform validation of the name and give a message if it isn't valid.
Here are the validations to apply:
1) You haven't typed in anything. Enter your full name.
2) The name is less than four characters. Please make sure you have entered 
your name and surname
3) It is too long (>25chars)
4) Thank you for entering a name.
"""

msg1 = "Please make sure that you have typed in both names."
msg2 = "Please make sure you haven't typed in too much."
msg3 = "You have not typed in anything?"
msg4 = "Thank you for entering your name"

def ask():
    """
    Takes no arguments, but returns the name input, name length, and a boolean set to False. 
    """
    nameBool = False
    name = (input("Please type in your full name..."))
    s_name = len(name)
    return name, s_name, nameBool

def run_code():
    """
    Assigns the name, name length, and a False boolean from the ask() function.
    Enters a loop based on the boolean. 
    Control structure to test for validation, re-asking questions and printing the correct messages. 
    The last condition is to escape the loop if all other conditions are met. 
    Finally, print the thank you message. 
    """
    n, l, b = ask()
    
    while not b:
        if l <= 6: 
            print(msg1)
            n, l, b = ask()
        elif l > 25:
            print(msg2)
            n, l, b = ask()
        elif l == 0:
            print(msg3)  
            n, l, b = ask()
        else: 
            b = True
    
    print(msg4)
      
                 
if __name__ == '__main__':
    run_code()