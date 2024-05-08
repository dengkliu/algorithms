# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        # 1 2 3 1
        # 0 3 mid = 1 
        # 1 3 mid = 2
        # 1 2
        while low + 1 < high:
            mid = (low + high) // 2
            # descending
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid
        
        return low if nums[low] > nums[high] else high