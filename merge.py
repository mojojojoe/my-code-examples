#!/usr/bin/env python3.11
List = list[int]
def merge(nums1:List, nums2: List) -> None:
    """
    Do not returun anything, modify nums1 in-place instead.
    """
    nums1 += nums2
    nums1 = sorted(nums1, reverse=True)


if __name__ == '__main__':
    num2 = [2,5,6,4,1]
    num1 = [1, 5, 2, 5, 4, 3]
    merge(num1, num2)
    print(num1)