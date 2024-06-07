# https://leetcode.com/problems/diagonal-traverse/

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # 0 - [0, 0]
        # 1 -  [0, 1], [1, 0]
        # 2 - [2, 0], [1, 1], [0, 2]
        # 3 - [1, 2], [2, 1]
        # 4 - [2, 2]

        if not mat or not mat[0]:
            return []

        # 1 - go up
        # -1 - go down
        DIRECTION = 1

        r = c = 0
        m = len(mat)
        n = len(mat[0])

        res = []

        while r in range(m) and c in range(n):
            res.append(mat[r][c])

            # we need to go up
            if DIRECTION == 1:
                while r - 1 in range(m) and c + 1 in range(n):
                    res.append(mat[r - 1][c + 1])
                    r = r - 1
                    c = c + 1
                # now we need to change and move to go down
                # we move to right element if it exists
                if c + 1 in range(n):
                    c = c + 1
                # we are at the last column
                elif r + 1 in range(m):
                    r = r + 1
                else:
                    return res
                DIRECTION = 0
            else:
                while r + 1 in range(m) and c - 1 in range(n):
                    res.append(mat[r + 1][c - 1])
                    r = r + 1
                    c = c - 1
                # now we need to change and move to go up
                # we move down if possible
                if r + 1 in range(m):
                    r = r + 1
                # otherwise we move right
                elif c + 1 in range(n):
                    c = c + 1
                else:
                    return res
                DIRECTION = 1
    