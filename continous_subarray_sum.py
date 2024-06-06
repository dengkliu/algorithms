# https://leetcode.com/problems/continuous-subarray-sum/

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) < 2:
            return False

        if k == 1:
            return True

        prefix_sum = 0
        mod_to_index = {}
        mod_to_index[0] = -1

        # [23,2,6,4,7]
        # {}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            residue = prefix_sum % k 
            if residue in mod_to_index:
                if i - mod_to_index[residue] > 1:
                    return True
                # why we don't need to update the index?
            else:
                mod_to_index[residue] = i
        
        return False