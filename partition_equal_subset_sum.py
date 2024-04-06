# https://leetcode.com/problems/partition-equal-subset-sum/description/

# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Input: nums = [1, 5, 11, 5], 
# Output: true
# Explanation:
# two subsets: [1, 5, 5], [11]

# 典型的背包问题
# 从一个set中 选取多少 达到一个和/目标

# dp --> len(nums) + 1, target + 1
# dp[0][0] = True
# dp[i][j] --> 前i个数，能否得到和j 选i的话 dp[i][j] = dp[i-1][j - nums[i]]
# 不选i的话 dp[i][j] = dp[i-1][j]
# 因此，当 j < nums[i] --> dp[i][j] = dp[i-1][j]
# 当 j >= nums[i] ----> dp[i][j] = dp[i-1][j - nums[i]] or dp[i-1][j]
# return dp[len(nums)][target]

class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        
        # 如果是奇数 直接返回False
        if sum%2 == 1:
            return False
        
        target = int(sum/2)
        n = len(nums)

        # 初始化二维数组
        dp = [[False] * (target + 1) for i in range(2)]

        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # i --> 前i个数 当前数为nums[i-1]
                if j < nums[i - 1]:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    dp[i%2][j] = dp[(i-1)%2][j] or dp[(i-1)%2][j - nums[i - 1]]
        
        return dp[n%2][target]




