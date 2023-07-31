"""
Running sum of a 1-D array.
--------------------------
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
def runningSum(nums):
    i = 0
    length = len(nums)-2
    while i <= length:
        nums[i + 1] = nums[i] + nums[i + 1]
        i += 1
    return nums

def main():
    print(runningSum(runningSum(runningSum([1,1,1,1,1,1,1]))))

if __name__ == '__main__':
    main()