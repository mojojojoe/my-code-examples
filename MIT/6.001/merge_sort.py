#!/usr/bin/env python3

def merge(a,b):
    pass
def mergesort(arr):
    """Recursively split the array into two"""
    l = len(arr)
    if l > 3:
        s = int(l/2)
        L = arr[:s]
        R = arr[s + 1:]
    elif l > 1:
        L = arr[:s]
        R = arr[s+1:]
    elif l == 2:
        merge(arr[1],arr[2])
    else:
        print("Error",l)
def sort(arr):
    mergesort(arr)

def main():
    C = [1, 2, 3, 5, 2, 0, 9, 2, 9, 5, 928, 58, 72, 72, 72, 5, 92, 91]
    sort(C)


if __name__ == '__main__':
    main()