# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(comb, result, curr, target, counter):

            if target == 0:
                result.append(list(comb))
                return
            # no negative numbers
            elif target < 0:
                return

            # why do we iterate through counter?
            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[next_curr] = (candidate, freq - 1)
                dfs(comb, result, next_curr, target - candidate, counter)
                counter[next_curr] = (candidate, freq)
                comb.pop()
    
        num_cnt = collections.defaultdict(int)
        for num in candidates:
            num_cnt[num] += 1
        counter = [(num, num_cnt[num]) for num in num_cnt]

        result = []
        dfs([], result, 0, target, counter)

        return result