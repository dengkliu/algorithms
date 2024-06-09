# https://leetcode.com/problems/diagonal-traverse/

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat:
            return []

        groups = collections.defaultdict(list)
        for row in range(len(mat) - 1, -1, -1):
            for col in range(len(mat[0])):
                diagnoal = row + col
                groups[diagnoal].append(mat[row][col])

        cur_diagnoal = 0
        diagonal_order = []
        while cur_diagnoal in groups:
            if cur_diagnoal % 2 == 0:
                diagonal_order.extend(groups[cur_diagnoal])
            else:
                diagonal_order.extend(groups[cur_diagnoal][::-1])
            cur_diagnoal += 1
        
        return diagonal_order
    