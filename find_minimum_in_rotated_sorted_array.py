# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        # There is no rotation
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] > nums[0]:
                start = mid
            elif nums[mid] < nums[0]:
                end = mid

        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]