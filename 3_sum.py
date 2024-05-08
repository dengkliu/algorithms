# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        dups = set()

        for i in range(len(nums)):
            num1 = nums[i]
            if num1 in dups:
                continue
            # say we have processed element 1 and found all the triplets sum to 0, 
            # including these that use other 1s from the list
            # we should skip all rest 1s in the list
            dups.add(num1)
            num_to_indice = {}
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                complement = - num1 - num2
                if complement in num_to_indice:
                    triplet = [num1, num2, complement]
                    triplet.sort()
                    result.add(tuple(triplet))
                num_to_indice[num2] = j
            
        return result