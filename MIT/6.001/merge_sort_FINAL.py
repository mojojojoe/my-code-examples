#!/usr/bin/env python3.11
"""merge_sort and merge derived from chatGPT"""
L 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


def merge(L, R):
    merged = []
    L_idx = 0
    R_idx = 0

    while L_idx < len(L) and R_idx < len(R):
        if L[L_idx] <= R[R_idx]:
            merged.append(L[L_idx])
            L_idx += 1
        else:
            merged.append(R[R_idx])
            R_idx += 1

    # Append any remaining elements
    while L_idx < len(L):
        merged.append(L[L_idx])
        L_idx += 1

    while R_idx < len(R):
        merged.append(R[R_idx])
        R_idx += 1

    return merged


def sort(M,args):
    if isinstance(args, list):
        return merge_sort(args)
    else:
        print("Error:args not a list")
        return None


def ask_for_list():
    # n = int(input("How long is the list?\n"))
    # D = []
    # i = 0
    # while n:
    #     item = int(input("Enter the next list item\n"))
    #     D.append(item)
    #     n -= 1
    D = [56, 72, 90, 100, 27, 982, 927, 2378, 287, 898, 90]
    return D


def main(args = None):
    if not args:
        ask = ask_for_list()
        main(ask)
    else:
        M = []
        M = sort(M,args)
        if M:
            print(M)


if __name__ == '__main__':
    main()
