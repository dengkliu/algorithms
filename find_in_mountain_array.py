# https://leetcode.com/problems/find-in-mountain-array/

# This problem contains 2 sub-problems, which are both basical binary search problem -
# 1. Find peak element in a mountian array
# 2. Find a number in a sorted array using binary search

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        peak_index = self._findPeak(mountain_arr)

        peak_num = mountain_arr.get(peak_index)

        if peak_num < target:
            return -1
        elif peak_num == target:
            return peak_index
        else:
            result = self._find(target, mountain_arr, 0, peak_index -1, True)
            if result != -1:
                return result
            else:
                return self._find(target, mountain_arr, peak_index, mountain_arr.length() -1, False)

    
    def _findPeak(self, arr):
        low = 0
        high = arr.length() - 1

        while low + 1 < high:
            mid = (low + high)//2
            if arr.get(mid) < arr.get(mid + 1):
                low = mid
            else:
                high = mid

        return low if arr.get(low) > arr.get(high) else high

    
    def _find(self, target, arr, start_index, end_index, ascending):
        low = start_index
        high = end_index

        while low + 1 < high:
            mid = (low + high)//2
            if arr.get(mid) > target:
                if ascending:
                    high = mid
                else:
                    low = mid
            else:
                if ascending:
                    low = mid
                else: 
                    high = mid
        
        if arr.get(low) == target:
            return low
        
        if arr.get(high) == target:
            return high

        return -1
