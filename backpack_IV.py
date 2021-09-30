# https://www.lintcode.com/problem/562/

# Give n items and an array, num[i] indicate the size of ith item. 
# An integer target denotes the size of backpack. 
# Find the number of ways to fill the backpack.

# Input: nums = [2,3,6,7] and target = 7
# Output: 2
# Explanation:
# Solution sets are: 
# [7]
# [2, 2, 3]

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    # dp[i][j] --> 在i这个地方 得到这个target有几种方法
    # 
    #        
    #   0 1 2 3 4 5 6 7
    #   1 0 0 0 0 0 0 0
    # 2 1 0 1 0 1 0 1 0
    # 3 1 0 1 1 1 0 2 1
    # 6 1 0 1 1 1 0 3 1
    # 7 1 0 1 1 1 0 0 2
    def backPackIV(self, nums, target):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)

        dp = [[0 for _ in range(target + 1)] for _ in range(2)]

        for i in range(n + 1):
            dp[i%2][0] = 1

        for item in range(1, n + 1):
            for size in range(1, target + 1):
                dp[item%2][size] = dp[(item - 1)%2][size]
                if (nums[item - 1] <= size):
                    dp[item%2][size] += dp[item%2][size - nums[item - 1]]
        
        return dp[n%2][target]