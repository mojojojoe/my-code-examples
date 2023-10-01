def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

# Example usage:
arr = [9, 3, 7, 1, 5, 6, 2, 8, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)
