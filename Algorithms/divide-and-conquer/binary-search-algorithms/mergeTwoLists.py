from array import array

def mergeTwoLists(arr1:array('I'), arr2: array('I')) -> array('I'):
    l1, l2 = len(arr1), len(arr2)
    if l1 > l2:
        long, short, ll, ls = arr1, arr2, l1, l2
    else:
        short, long, ls, ll = arr1, arr2, l1, l2

    L = []
    while long:
        while short:
            sp = short.pop()
            lp = long.pop()
            if sp > lp:
                L.append(sp)
                L.append(lp)
            else:
                L.append(lp)
                L.append(sp)
        L.append(long.pop())
    return L

def main():
    L1, L2 = array('I'), array('I')
    L1 = [10, 7, 6, 4, 3, 2, 1]
    L2 = [15, 11, 10, 5, 3, 2]
    mergedList = mergeTwoLists(arr1=L1,arr2=L2)
    print(mergedList)

if __name__ == '__main__':
    main()