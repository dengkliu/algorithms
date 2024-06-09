# https://leetcode.com/problems/diagonal-traverse-ii/

# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        groups = collections.defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagnoal = row + col
                groups[diagnoal].append(nums[row][col])

        cur_diagnoal = 0
        diagonal_order = []
        while cur_diagnoal in groups:
            diagonal_order.extend(groups[cur_diagnoal])
            cur_diagnoal += 1
        
        return diagonal_order