# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def k_sum(nums, target, k):
            res = []
            if not nums:
                return nums
            
            avg = target//k
            if avg < nums[0] or avg > nums[-1]:
                return res

            if k == 2:
                return two_sum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in k_sum(nums[i + 1:], target - nums[i], k -1):
                        res.append([nums[i]] + subset)
            
            return res

        
        def two_sum(nums, target):
            res = []
            low, high = 0, len(nums) - 1
            while low < high:
                num = nums[low] + nums[high]
                if num < target or (low > 0 and nums[low] == nums[low - 1]):
                    low += 1
                elif num > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                    high -= 1
                else:
                    res.append([nums[low], nums[high]])
                    low += 1
                    high -= 1
            
            return res


        nums.sort()

        return k_sum(nums, target, 4)