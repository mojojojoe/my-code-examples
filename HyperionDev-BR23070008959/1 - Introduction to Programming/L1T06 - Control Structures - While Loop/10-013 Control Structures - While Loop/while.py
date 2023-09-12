#!/usr/bin/env python3

def do_a_while():
    """
    Input: An integer from std input
    Output: A running average is printed to stdout
    A loop that runs until '-1' is typed in and prints
    out the running sum divided by the running count. I.e., the
    running average.
    """
    i = 0
    num = 0
    tot = 0
    while num != -1:
        i += 1
        tot += num
        print (f"The average is {tot/i}") 
        num = int (input ("Please type in any number other than -1:\n"))
   

if __name__ == "__main__":

    do_a_while()
