# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Input: [2,3,1,2,4,3], target = 7
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# O(N) time complexity
# O(1) space complexity
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        result = float('inf')
        subarray_sum = 0

        #  [2,3,1,2,4, 3]
        #  0 2 5 6 8 12 15
        for start in range(0, len(nums)):           
            while end < len(nums) and subarray_sum < target:
                subarray_sum += nums[end]
                end += 1
                
            if subarray_sum >= target:
                result = min(end - start, result)
                
            subarray_sum -= nums[start]
        
        return 0 if result == float('inf') else result
