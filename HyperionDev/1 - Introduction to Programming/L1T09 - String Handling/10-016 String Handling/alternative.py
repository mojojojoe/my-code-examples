#!/usr/bin/env python3

def alt_upper_lower(str):
    """
    input: a string
    output: a string
    algorithm:
    convert the string to a list 
    iterate over the list with enumerate to extract the count
    for each character reassign the string list to lowercase if the character is uppercase
    otherwise assign it to uppercases
    out of the loop, join the list together again into a string and return it
    """
    from curses.ascii import isupper
    stra = list(str)
    for count, char in enumerate(stra):
        stra[count] = char.lower() if isupper(char) else char.upper()
    return "".join(stra)

def second_task(str):
    """_summary_

    Args:
        str (string): the string array to be fondled

    Returns:
        string: the fondled string
    
    Pseudocode:
        split the string into an array of words
        iterate over the array applying a control as follows:
            if the index value is even then make the word uppercase,
            otherwise make the word lowercase
        outside the loop join the array back into a string and return it
    """
    splita = str.split(" ")
    for count, itm in enumerate(splita):
        # capitalize oddly indexed item
        splita[count] = itm.upper() if count % 2 == 1 else itm.lower()
    return " ".join(splita)


if __name__ == "__main__":
    """ 
    Create two strings of arb wording
    pass them through their respective functions and print the output
    """
    input_string = "in the Beginning was the WORD"
    second_input = "Oh there ye BLOW" 
    # = input ("Please type in a sequence of characters: ")
    print (alt_upper_lower (input_string))
    print(second_task(second_input))