# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            
            curr_l, curr_r = 0, 0
            if root.left and root.val == root.left.val:
                curr_l = 1 + l
            if root.right and root.val == root.right.val:
                curr_r = 1 + r
            
            result[0] = max(result[0], curr_l + curr_r)

            return max(curr_l, curr_r)

        dfs(root)

        return result[0]
