# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = [0]

        def dfs(root):

            l = 0
            r = 0

            if root.left:
                l = dfs(root.left) + 1
            if root.right:
                r = dfs(root.right) + 1

            result[0] = max(result[0], l + r)

            return max(l, r)

        dfs(root)

        return result[0]  
