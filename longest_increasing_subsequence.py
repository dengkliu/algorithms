# https://www.lintcode.com/problem/76/

# Given a sequence of integers, find the longest increasing subsequence (LIS).

# You code should return the length of the LIS.

# nums = [4,2,4,5,3,7]
# 4

# dp[i] = max(dp[k] + 1, if nums[k] < nums[i-1])
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # dp[i] dp[i-1]
    def longestIncreasingSubsequence(self, nums):

        if not nums or len(nums) == 0:
            return 0
        
        dp = [1 for _ in range(len(nums))]

        result = 0

        for i in range(0, len(nums)):
            for j in range(0, i):
                # 假如 nums[i] 比 nums[j]大，则可试着接在其后
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
            
            result = max(result, dp[i])
        
        return result