# https://www.lintcode.com/problem/77

# Given two strings, find the longest common subsequence (LCS).
# Your code should return the length of LCS.

# The longest common subsequence problem is to find the longest common subsequence in a set of sequences (usually 2). 
# This problem is a typical computer science problem, which is the basis of file difference comparison program, 
# and also has applications in bioinformatics.

# A = "ABCD"
# B = "EDCA"

# 1

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    # dp[i][j] -- A前i个字母和B前j个字母的最长公共子序列
    # if A[i-1] == B[j-1] dp[i][j] = dp[i-1][j-1] + 1
    # if A[i-1] != B[j-1] dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    def longestCommonSubsequence(self, A, B):
        # write your code here

        n = len(A)
        m = len(B)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]

