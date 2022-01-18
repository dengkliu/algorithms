# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# 因为都是正整数
# 向右多加一个数 和一定增加
# 向左多减一个数 和一定减少
# 用同向的两个指针 来追踪所有以start为开头的满足条件的最小array
# O(N)
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        start, end = 0, 0
        result = float('inf')
        subarray_sum = 0

        #   [2,3,1,2,4, 3]
        #  0 2 5 6 8 12 15
        for start in range(0, len(nums)):           
            while end < len(nums) and subarray_sum < s:
                subarray_sum += nums[end]
                end += 1

            if subarray_sum >= s:
                result = min(end - start, result)
            else:
                return -1 if result == float('inf') else result
            
            subarray_sum -= nums[start]
        
        return -1 if result == float('inf') else result
