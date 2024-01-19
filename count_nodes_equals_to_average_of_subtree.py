# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

# Count Nodes Equal to Average of Subtree
# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

# Note:
# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]

        def helper(root):

            if root is None:
                return (0, 0)

            sum_val_l, node_count_l = helper(root.left)
            sum_val_r, node_count_r = helper(root.right)

            sum_val = sum_val_l + sum_val_r + root.val
            node_count = node_count_l + node_count_r + 1

            average = sum_val//node_count
            
            if root.val == average:
                result[0] = result[0] + 1
            
            return (sum_val, node_count)
        
        helper(root)
        return result[0]




