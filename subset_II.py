
# https://www.lintcode.com/problem/18/
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

#2. DFS
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    # dp[i] -- 前i个数的结果
    def subsetsWithDup(self, nums):

        nums = sorted(nums)
        
        result = []

        result.append([])

        # 每次需要的组合数目不一样，但是终止条件是一样的
        for i in range(1, len(nums) + 1):
            curr_set = []
            self.dfs(nums, result, 0, i, curr_set)
        
        return result

    def dfs(self, nums, result, start, num_cnt, curr_set):
        
        if len(curr_set) == num_cnt:
            result.append(list(curr_set))
            return

        for i in range(start, len(nums)):
            # 去重 没那么简单哦
            # 假如这个数字本身是start 那是无论如何都要加入的
            # 只有在考虑了这个数字本身之后 后面遇到的重复的 才不考虑
            if i > start and nums[i] == nums[i-1]:
                continue

            curr_set.append(nums[i])
            # 一定要注意，这里的下一个index是 i + 1 而不是start + 1
            self.dfs(nums, result, i + 1, num_cnt, curr_set)
            curr_set.pop()