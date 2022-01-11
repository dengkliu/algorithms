# https://www.lintcode.com/problem/390

# Given an integer matrix A which has the following features :
# The numbers in adjacent positions are different.
# The matrix has n rows and m columns, n and m will not less than 3.
# For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
# For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]

# We define a position [i, j] is a peak if:
# A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] && 
# A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]

# Input: 
#    [
#      [1, 2, 3, 6,  5],
#      [16,41,23,22, 6],
#      [15,17,24,21, 7],
#      [14,18,19,20,10],
#      [13,14,11,10, 9]
#    ]
# Output: [1,1]
# Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.

# Binary search can be used to find a local minimum or maximum.
# A local minimum or maximum means it is smaller or larger than its neighbor

class Solution:
    """
    @param A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here

        row_cnt = len(A)
        col_cnt = len(A[0])

        for i in range(1, row_cnt -1):
            local_max_col = self.__find_local_max(A[i])
            if A[i-1][local_max_col] < A[i][local_max_col] and A[i+1][local_max_col] < A[i][local_max_col]:
                return [i, local_max_col]

        return None

        # 13, 14, 8, 11, 8, 9
        # 0,  1,  2, 3, 4,  5
        # mid -- 8, 8 < 14, end = mid
        # else: start = mid

    # Use binary search to find the local maximum
    # For a number which is smaller than its left neighor, 
    # it is guarantee that a local maximum exists on the left side
    def __find_local_max(self, row):
        start, end = 0, len(row)-1

        while start + 1 < end:
            mid = (start + end)//2
            if row[mid] < row[mid-1]:
                end = mid
            else:
                start = mid
        
        return start if row[start] > row[end] else end