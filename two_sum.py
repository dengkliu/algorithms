# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_to_indice = {}

        for i in range(len(nums)):
            if target - nums[i] in number_to_indice:
                return [number_to_indice[target - nums[i]], i]
            number_to_indice[nums[i]] = i
        
        return None