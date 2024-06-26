# https://leetcode.com/problems/house-robber-iii/

# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            # Why here we take the max of both left and right?
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        
        return max(dfs(root))