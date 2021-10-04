# https://www.lintcode.com/problem/1800/

# Given an array of A, a non-negative integer target. 
# Each decimal in A needs to be operated by ceil or floor, and finally an integer array is obtained, 
# requiring the sum of all integers that are in the array to be equal to target, and requiring adjustments sum of the decimal array is minimum.
# Such as ceil(1.2),adjustment is 0.8,floor(1.2),adjustment is 0.2. return the integer array.

# 1.1<=A.length<=300
# 2.0<=target<=15000
# 3.0.0<=A[i]<=100.0
# 4.Datas guarantees the existence of answers.

# Input：A=[1.2,1.3,2.3,4.2],target=9
# Output：[1,1,3,4]
# Explanation：1.2->1,1.3->1,2.3->3,4.2->4.

import math

class Solution:
    """
    @param A: A float array
    @param target: A non-negative integer
    @return: Return an integer array which sum equals target
    """
    # dp[i][j] -- the minimal adjustments sum that you can get 
    # when you have i numbers and target is j
    # dp[i][j] = min(dp[i-1][j- ceiling(A[i-1]), dp[i-1][j-flooring(A[i-1])]])
    #       0  1   2 3 4 5 6 7 8 9
    # 0     0  0   0 0 0 0 0 0 0 0
    # 1.2   0 0.2
    # 1.3   0
    # 2.3   0
    # 4.2   0
    def getArray(self, A, target):
        
        if not A or len(A) == 0:
            return 0

        n = len(A)

        dp = [[float('inf') for _ in range(target + 1)] for _ in range(n + 1)]

        # 用另外一个矩阵记录在每个dp[i][j]时候的选择 1 表示往上取 0 表示往下取
        prev = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            
            adjustments_ceiling = float('inf')
            adjustments_flooring = float('inf')
            ceiling = math.ceil(A[i-1])
            flooring = math.floor(A[i-1])
            
            for j in range(target + 1):
                
                if ceiling <= j:
                    adjustments_ceiling = dp[i-1][j-ceiling] + ceiling - A[i-1]
                    if adjustments_ceiling < dp[i][j]:
                        dp[i][j] = adjustments_ceiling
                        prev[i][j] = 1
                
                if flooring <= j:
                    adjustments_flooring = dp[i-1][j-flooring] + A[i-1] - flooring              
                    if adjustments_flooring < dp[i][j]:
                        dp[i][j] = adjustments_flooring
                        prev[i][j] = 0

        result = []
        target_remaining = target

        # 从 A[n-1]和target开始 往前回溯
        for i in range(n, 0, -1):
            curr_num = A[i - 1]
            if prev[i][target_remaining] == 1:
                result.insert(0, math.ceil(curr_num))
                target_remaining = target_remaining - math.ceil(curr_num)
            else:
                result.insert(0, math.floor(curr_num))
                target_remaining = target_remaining - math.floor(curr_num)

        return result

