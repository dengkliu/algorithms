# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates:
            return 0

        result = [0]

        def dfs(comb, target, nums, cur, result):
            if target == 0:
                result.append(list(comb))
            
            if target < 0:
                return

            # why do we start from cur instead of cur + 1?
            # because we can reuse the same number unlimited of times
            for next_cur in range(cur, len(nums)):
                comb.append(nums[next_cur])
                # why do we pass next_cur to recursion?
                # for the recurison we want to start with next_cur
                dfs(comb, target - nums[next_cur], nums, next_cur, result)
                comb.pop()

        result = []

        dfs([], target, candidates, 0, result)

        return result