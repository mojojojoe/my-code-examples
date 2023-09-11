#!/usr/bin/env python3.11



def divideAndConquer(L:list)->list:
    end = len(L)
    m = end // 2
    if end > 2:
        divideAndConquer(L[m:])
        divideAndConquer(L[:m])
    elif end == 2:
        a = L.pop()
        b = L.pop()
        if b > a:
            L.append(b)
            L.append(a)
        else:
            L.append(a)
            L.append(b)
    return L

def mergeTwoLists(one,two):
    for i in two:
        one.append(i)
    return divideAndConquer(one)

def main():
    A, B = [], []
    A = [20,17,14,11,8,5,3,2,1]
    B = [22,20,18,16,14,12,10,8,6,4,2]
    print(mergeTwoLists(A,B))
 
if __name__ == '__main__':
    main()