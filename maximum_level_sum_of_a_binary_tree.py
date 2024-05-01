# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 1
        
        queue = collections.deque()
        queue.append(root)
        level = 1
        max_level_sum = float('-inf')
        result = 0

        while queue:
            size = len(queue)
            cur_level_sum = 0
            for i in range(size):
                node = queue.popleft()
                cur_level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cur_level_sum > max_level_sum:
                result = level
                max_level_sum = cur_level_sum
            level += 1
        
        return result