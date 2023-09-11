#!/usr/bin/env python3.11

"""
By executing the first_program method, the user should:
 1} be prompted for their name using input() and assignment to name variable
 2) have their name presented to them with the print function
 3) be prompted for their age using the input function
 4) have their age and name presented and couched in a sentence with the fstring method inside print.
"""
"""
The pseudocode provided by the author follows:
1. the input name is derived from user input from a prompt
2. the program pauses for 5 seconds
3. another prompt appears asking for user age
4. the program pauses for another 5 seconds
5. A friendly message is printed using an f-string in the print function.
"""



import time

def first_program() -> int:
    name = input("Please type in your name: ")#needs checking for surrounding space and capitalization, perhaps also validation as a proper name.
    time.sleep(5)
    age = int(input(f"{name} please type in your age: "))
    time.sleep(5)
    print(f'''
          Sloth says, \n 
          \"In a century 
              {name} 
                will be 
                  {age+100} years old. 
                
          Sleep tight {name}!\"''')
    return 0


if __name__ == '__main__':
    first_program()
