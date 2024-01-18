
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root:
            return root
        
        
        l = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        r = self.lowestCommonAncestor(root.right, p, q) if root.right else None

        if l and r:
            return root
        
        return l or r 