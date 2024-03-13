# https://leetcode.com/problems/symmetric-tree/description/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Input: {1,2,2,3,4,4,3}
# Output: true
# Explanation:
#    1
#   / \
#  2   2
# / \ / \
# 3  4 4  3
# This binary tree {1,2,2,3,4,4,3} is symmetric
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Time complexity O(N) -- we are checking all the nodes
# Space complexity O(N) -- in worst case the tree is linear and height is O(N) (?)
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.is_symmetric_tree_helper(root.right, root.left)

        # Write your code here

    def is_symmetric_tree_helper(self, node1, node2):
        
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.is_symmetric_tree_helper(node1.left, node2.right) and \
        self.is_symmetric_tree_helper(node1.right, node2.left)
