#!/usr/bin/env python3

def add_ints():
    A = []
    i = 0
    while (i<3):
        A.append(int(input("Please enter a number")))
        i += 1
        
    print(sum(A))
    print(A[0]-A[1])
    
    
if __name__ == '__main__':
    add_ints()