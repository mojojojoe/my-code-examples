#!/usr/bin/env python3

def manipulate():
    str_manip = input("Please type in a stromg of characters, or sentence: ")
    n_str_manip = len(str_manip)
    print(f"The length of your string is: {n_str_manip}\n")
    last_letter = str_manip[-1]
    print(f"The last letter is {last_letter}\n")
    rep_str_manip = str_manip.replace(last_letter, "@")
    print(f"The replaced characters are: {rep_str_manip}\n")
    last3 = str_manip[-1:-4:-1]
    print(f"The last three characters of the string are: {last3}\n")
    f3 = str_manip[0:3:1]
    l2 = str_manip[-2:n_str_manip:]
    print(f3 + l2)
    
if __name__ == '__main__':
    manipulate()