# https://leetcode.com/problems/3sum-smaller/

# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nlog(n)
        nums.sort()
        result = 0

        def two_sum_smaller(nums, start, target):
            low = start
            high = len(nums) - 1
            result = 0
            while low < high:
                if nums[low] + nums[high] < target:
                    result += high - low
                    low += 1
                else:
                    high -=1
            return result

        for i in range(0, len(nums) - 2):
            result += two_sum_smaller(nums, i + 1, target - nums[i])
        
        return result