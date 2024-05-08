# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            num1 = nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] + num1 == target:
                    return target
                else:
                    if abs(diff) > abs(nums[low] + nums[high] + num1 - target):
                        diff = nums[low] + nums[high] + num1 - target
                    
                    if nums[low] + nums[high] + num1 > target:
                        high -= 1
                    else:
                        low += 1
        
        return target + diff
