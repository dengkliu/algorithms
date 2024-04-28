# https://leetcode.com/problems/balanced-binary-tree/description/

# Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def dfs(root):
            if not root:
                return (True, 0)
            l, l_h = dfs(root.left)
            r, r_h = dfs(root.right)

            if l and r:
                return (abs(l_h - r_h) <= 1, max(l_h, r_h) + 1)
            else:
                return (l and r, max(l_h, r_h) + 1)

        result, height = dfs(root)

        return result   