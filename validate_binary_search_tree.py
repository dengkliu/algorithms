# https://www.lintcode.com/problem/95/
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST

# Divide and conquer.
# A tree is valid BST only if its left child and right child is valid BST 
# And the all left children is smaller than it and all right children is greater than it.
# A top down solution

#
# Definition of TreeNode:
# public class TreeNode {
#     public int val;
#     public TreeNode left, right;
#     public TreeNode(int val) {
#        this.val = val;
#        this.left = this.right = null;
#     }
# }

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        
        if root is None:
            return True

        max_limit = float('inf')
        min_limit = float('-inf')

        return self.isValidNode(root.left, root.val, min_limit) and \
        self.isValidNode(root.right, max_limit, root.val)
    
    def isValidNode(self, node, max_limit, min_limit):
        if node is None:
            return True

        if node.val <= min_limit or node.val >= max_limit:
            return False
        
        return self.isValidNode(node.left, node.val, min_limit) and \
        self.isValidNode(node.right, max_limit, node.val)
