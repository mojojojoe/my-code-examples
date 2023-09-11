#!/usr/bin/env python

def alt_upper_lower(str):
    """
    Input: A string
    Output: A string with all even characters capped and all uneven characters uncapped.
    Pseudo code:
    Prepare variables: create two arrays to hold the split string, a counter and the index cap
    Loop: over string, decided whether character is evenly or oddly placed. If even, append to first array,
            if odd append to second array.
    Map join section:
        take the first array and map a the emptry string join function over it, causing all the elements of a to be 
        joined to the empty string. i.e. convert the array a to a list of strings. 
        then, join all the string elements of the array to an empty string. Once the string exists,
        UPPERCASE it. Do this likewise with the second array.
    Finally:
        Zip the two string arrays. This creats an object which has to be mapped to a string with "".join
    Return the result and print it out in the main function.
    """
    cap = len(str)
    i = 0 
    # create two empty arrays to use 'append' in the loop
    a = []
    b = []
    # split the string into two alternating strings...
    while(i < cap):
        if i % 2 == 0:
            a.append(str[i])    
        else:
            b.append(str[i])
        i += 1
    # map the upper and lower functions to the split strings
    a = "".join(map("".join,a)).upper()
    b = "".join(map("".join,b)).lower()
    # re-merge the two strings
    return "".join(map("".join,zip(a, b)))
    


if __name__ == "__main__":
    s = input ("Please type in a sequence of characters: ")
    print (alt_upper_lower (s))
