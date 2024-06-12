# https://leetcode.com/problems/toeplitz-matrix/

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """    
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        
        return True        
        

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        pre_row = matrix[0][:-1]
        for r in range(1, len(matrix)):
            cur_row = matrix[r][1:]
            if pre_row != cur_row:
                return False
            pre_row = matrix[r][:-1]
        
        return True