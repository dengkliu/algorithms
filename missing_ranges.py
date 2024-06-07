# https://leetcode.com/problems/missing-ranges/

# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        if not nums:
            return [[lower, upper]]

        p = 0
        res = []

        if nums[p] > lower:
            res.append([lower, nums[p] - 1])

        while p < len(nums) - 1:
            if nums[p + 1] - nums[p] > 1:
                res.append([nums[p] + 1, nums[p + 1] -1])
            p += 1

        if nums[p] < upper:
            res.append([nums[p] + 1, upper])

        return res

# [0, 1, 3, 50, 75] 0, 99
# [[2, 2], [4, 49], [51, 74], [76, 99]]