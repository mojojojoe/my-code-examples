def comp_merge(M, L, R):
    """Here a list of length 1 is input
    merge by popping the smallest item between the top of the two lists into a the merged list"""
    if L[0] >= R[0]:
        M.append(R.pop(0))
        M.append(L.pop(0))
    else:
        M.append(L.pop(0))
        M.append(R.pop(0))
    return M

def split_merge(list):
    l = len(list)
    m = int(l / 2)
    L = []
    R = []
    Mer = []1
    L, R = list[:m], list[m:] # split list
    while(len(L) != 1 or len(R) != 1):
        split_merge(L)
        split_merge(R)
    comp_merge(Mer, L, R)

def ask_for_list():
    # n = int(input("How long is the list?\n"))
    # D = []
    # i = 0
    # while n:
    #     item = int(input("Enter the next list item\n"))
    #     D.append(item)
    #     n -= 1
    D = [56, 72, 90, 100, 27]
    return D

def sort(M,args):
    if isinstance(args, list):
        return split_merge(args)
    else:
        print("Error:args not a list")
        return None

def main(args = None):
    if not args:
        ask = ask_for_list()
        main(ask)
    else:
        M = []
        M = sort(M,args)
        if sorted:
            for idx,item in enumerate(sorted):
                print(f"{idx,item}\n")


if __name__ == '__main__':
    main()
