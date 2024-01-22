# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Input:
# tree = {1,2,3}
# Output:
# 6

# Divide and conquer
# For each node, the maximum path is 
# 1) the solution on its left subtree
# 2) the solution on its right subtree
# 3) the maximum path ending at its left child + the maximum path ending at its right child + its value
# There can be negative sum, always compare with 0

#
# Definition of TreeNode:
# public class TreeNode {
#     public int val;
#     public TreeNode left, right;
#     public TreeNode(int val) {
#         this.val = val;
#         this.left = this.right = null;
#     }
# }

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = [float('-inf')]
        
        def maxPathSumHelper(root):
            if not root:
                return 0
            
            max_l = maxPathSumHelper(root.left)
            max_r = maxPathSumHelper(root.right)

            result[0] = max(result[0], max_l + max_r + root.val)

            return max(max_l + root.val, max_r + root.val, 0)

        maxPathSumHelper(root)

        return result[0]
