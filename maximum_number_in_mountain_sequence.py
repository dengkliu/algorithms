# https://www.lintcode.com/problem/585

# Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).
# Arrays are strictly incremented, strictly decreasing. 这个先决条件很重要。

# Input: nums = [1, 2, 4, 8, 6, 3] 
# Output: 8

# Find the first num that the next number is smaller
# O(N) - scanning the array
# O(logN)Use binary search to narrow down

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        
        # variable defined in same line separated by comma
        # get length of array or list in python, use len()
        start, end = 0, len(nums) - 1

        # start + 1 < end is used to avoid infinite loop
        # (start + end) // 2 can get start. When the target is at the last position, there will be infinite loop
        # like nums = [1, 1] and target is 1
        while start + 1 < end: 
            
            # python // operation rounds the result down to the nearest whole number
            mid = (start + end) // 2

            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        return nums[end] if nums[start] < nums[end] else nums[start]
