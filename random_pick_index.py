# https://leetcode.com/problems/random-pick-index/

# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_indexes = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.num_indexes[num].append(i)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indexes = self.num_indexes[target]
        return indexes[random.randint(0, len(indexes) - 1)]