#!/usr/bin/env python3

import math

def area_triangle():
    A = []
    i = 0
    while (i<3):
        A.append(int(input("Please type in the length of a triangle side")))
        i += 1
        
    s = sum(A)/2
    area = math.sqrt(s * (s - A[0]) * (s - A[1]) * (s - A[2]))
    
    return area
    
if __name__ == '__main__':
    print(area_triangle())