# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

# Example
# array = [4, 5, 1, 2, 3]
# target = 1

# Brute force - O(N)
# Binary search - 因为旋转过，所以单调性被破坏了
# 这样可以找到那个最大的值，把两边分成两个单调区间，再进行binary search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_cut_position(nums):
            start, end = 0, len(nums) - 1
            
            while start + 1 < end:
                mid = (start + end)//2
                if nums[mid] > nums[0]:
                    start = mid
                else:
                    end = mid
            
            if nums[end] > nums[0]:
                return end
            else:
                return start
        
        def binary_search(target, nums, start, end):
            # the right side doesn't exist
            if start > end:
                return -1 
            
            while start + 1 < end:
                mid = (start + end)//2
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            
            if nums[start] == target:
                    return start
            
            if nums[end] == target:
                    return end
            
            return -1
        
        if not nums:
            return - 1

        # find pivot by binary search
        # the cut must be at a position that the number left of the cut is larger than the head of array
        # and the number right of the cut is small than the end of the array
        cut_position = find_cut_position(nums)
        # search the target with binary search either on left part or on the right part
        if target > nums[0]:
            return binary_search(target, nums, 0, cut_position)
        elif target < nums[0]:
            return binary_search(target, nums, cut_position + 1, len(nums) - 1)
        else:
            return 0
            