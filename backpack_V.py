# https://www.lintcode.com/problem/563/

# Given n items with size nums[i] which an integer array and all positive numbers. 
# An integer target denotes the size of a backpack. Find the number of possible fill the backpack.
# Each item may only be used once

# Given candidate items [1,2,3,3,7] and target 7,
# A solution set is: 
# [7]
# [1, 3, 3]
# return 2

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
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
                    dp[item%2][size] += dp[(item - 1)%2][size - nums[item - 1]]
        
        return dp[n%2][target]