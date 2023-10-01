import math

def merge_sort(arr):
    l = len(arr)
    m = math.ceil(l/2)
    while l > 2:
        merge_sort(arr[:m]),\
        merge_sort(arr[m:])
    MERGE()

def main():
    a = [45, 65, 89, 82, 23, 43]
    merge_sort(a)


if __name__ == '__main__':
    main()