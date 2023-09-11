#!/usr/bin/env python3
"""
Input: None
Output: print to stdout
A function to print a star chart.
The algorithm loops through a range of 1 to 10.
If in the i-th loop i is less than or equal to five,
then i stars are printed. After the fifth loop, 10-i stars
are printed, with the resulting pattern.
"""
def star_task():
    for i in range (1,10):
        if i <= 5:
            print (i * '*')
        else:
            print ((10 - i) * '*')

if __name__ == "__main__":
    star_task()
