# Given a collection of integers that might contain duplicate numbers, return all possible subsets.

# Each element in a subset must be in non-descending order.
# The ordering between two subsets is free.
# The solution set must not contain duplicate subsets.

# 1. DP
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    # dp[i] -- 前i个数的结果
    def subsetsWithDup(self, nums):

        nums = sorted(nums)
        
        # write your code here
        number_position = {}
        dp = []
        for i in range (0, len(nums) + 1):
            dp.append([])
        dp[0].append([])

        for i in range(1, len(nums) + 1):
            if nums[i-1] in number_position:
                prev_position = number_position[nums[i-1]]
                for j in range (prev_position + 1, i):
                    n = len(dp[j])
                    for k in range(n):
                        new_list = list(dp[j][k])
                        new_list.append(nums[i-1])
                        dp[i].append(new_list)
            else:
                for j in range(0, i):
                    n = len(dp[j])
                    for k in range(n):
                        new_list = list(dp[j][k])
                        new_list.append(nums[i-1])
                        dp[i].append(new_list)

            number_position[nums[i-1]] = i - 1

        result=[]

        for i in range(0, len(nums) + 1):
            print(i)
            print(len(nums) + 1)
            print(len(dp))
            result += dp[i]

        return result