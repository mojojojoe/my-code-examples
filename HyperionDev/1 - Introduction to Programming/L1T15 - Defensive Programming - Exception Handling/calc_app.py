#!/usr/bin/env python

def create_string(in:list)->str:
    """
    A key map is held in this function as a reference for four special characters lookups,
    If the particular operator is present return the functional string associated with it 
    for printing in the calling function.
    """
    operators = {
        '+':f"{in[1]} + {in[2]} = {in[1]+in[2]}\n",
        '-':f"{in[1]} - {in[2]} = {in[1]-in[2]}\n",
        '/':f"{in[1]} / {in[2]} = {in[1]/in[2]}\n",
        '*':f"{in[1]} * {in[2]} = {in[1]*in[2]}\n"
    }
    if in [0] in operators:
        return operators[in [0]]
    else:
        raise TypeError("Please enter one of the four algebraic operators [+,-,* or /]")

def get_input ():
    """
    This function compartmentalises the input functionality
    """
    n1 = input ("Please type in the first number ")
    op = input ("Please type in the operator ")
    n2 = input ("Please type in the second number ")
    
    if n1.isnumeric() is False: raise TypeError("Please make sure to type in a numeral")
    if n2.isnumeric() is False: raise TypeError("Please make sure to type in a numeral")
    
    return  [str (op), int (n1), int (n2)] 

def calculator():
    """
    Algorithm pseudocode:
    In a try block and within that within a loop,
       get input
       create the string from the input 
       print it
       store it temporarily in a list, to await folding out again at file write time
       ask if you want to quit and perform the functionality for that
    On quitting, open a file
       print each equation from the list to the file

    """
    q = []
    try:
        exit_loop = False
        while not exit_loop:
            incoming = get_input ()
            the_string = create_string(incoming)
            print(the_string)
            q.append(the_string)
 
            if input("Do you want to quit? ").upper() == "Y":
                exit_loop = True
                
        with open('equations.txt', 'w+') as fh_out:
            for item in q:
                fh_out.write(item)
                
    except FileNotFoundError:
        print("Cant find the file")
    except TypeError:
        print ("TypeError: one of the inputs took the wrong kind of input. Either an character where there should have been a number, or an uncasteable character.")
    except NameError:
        print("Please type in the correct operator next time")


if __name__ == "__main__":
    calculator()
