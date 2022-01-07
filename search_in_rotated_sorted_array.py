# https://www.lintcode.com/problem/62/
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

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here

        if not A:
            return -1

        # find pivot by binary search
        # the cut must be at a position that the number left of the cut is larger than the head of array
        # and the number right of the cut is small than the end of the array
        cut_position = self.__find_cut_position(A)
        # search the target with binary search either on left part or on the right part
        if target > A[0]:
            return self.__binary_search(target, A, 0, cut_position)
        elif target < A[0]:
            return self.__binary_search(target, A, cut_position + 1, len(A) - 1)
        else:
            return 0

    def __find_cut_position(self, A):
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] > A[0]:
                # we are still at the left side
                start = mid
            elif A[mid] < A[0]:
                end = mid
            else:
                end = mid

        if A[end] > A[0]:
            return end
        else:
            return start

    def __binary_search(self, target, A, start, end):

        # the right side doesn't exist
        if start > end:
            return -1 

        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        
        return -1

       
