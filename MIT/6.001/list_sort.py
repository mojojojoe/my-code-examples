
def find_max(lst):
    """ Take a list, get the max element by going over each item in the list and stashing the largest.
    Otherwise, append the item to a new (reduced) list to return with the max.
    """
    sortlist = []
    reduced = []
    max = 0
    for item in lst:
        if item > max:
            max = item
        else:
            reduced.append(item)
        return max, reduced

def gather_input():
    j = 0
    _list_ = []
    while j < 6:
        _list_.append(int(input("number?")))
        j += 1
    return _list_

def sort(list):
    sorted_list = []
    while list:
        max, list = find_max(list)
        sorted_list.append(max)
    return sorted_list
def __main__():
    print(sort(gather_input()))

if __name__ == '__main__':
    __main__()