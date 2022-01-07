# https://www.lintcode.com/problem/183/
# Given n pieces of wood with length L[i] (integer array). 
# Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
# What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

# Input [232, 124, 456]
# K = 7
# Output: 114

# We don't know what would the maximum length can be
# but we know the boundary
# it at least should be 1
# and at most as much as the max number in the array
# So we can do binary search in the solution space

class Solution:
    
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):

        if not L:
            return 0
        
        # write your code here
        max_length = self.__get_max_length(L)

        start, end = 0, max_length

        while start + 1 < end:
            mid = (start + end)//2
            if self.__can_make(mid, L, k):
                start = mid
            else:
                end = mid
        
        if self.__can_make(end, L, k):
            return end
        
        if start == 0:
            return 0
        elif self.__can_make(start, L, k):
            return start

        return 0

    def __get_max_length(self, L):

        max_length = float('-inf')

        for wood_length in L:
            if wood_length > max_length:
                max_length = wood_length

        return max_length
    
    def __can_make(self, length, L, k): 
        wood_cnt = 0
        
        for wood_length in L:
            wood_cnt = wood_cnt + wood_length//length

        if wood_cnt < k:
            return False

        return True