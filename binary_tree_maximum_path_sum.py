# https://www.lintcode.com/problem/94

# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
# (Path sum is the sum of the weights of nodes on the path between two nodes.

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
    @return: An integer
    """
    def maxPathSum(self, root):

        # define a global variable
        self.maximum_path = float('-inf')

        if root is None:
            return 0

        maximum_path_left_child = max(0, self.max_path_starting_from_root(root.left))

        maximum_path_right_child = max(0, self.max_path_starting_from_root(root.right))

        new_path_through_root = maximum_path_left_child + maximum_path_right_child + root.val

        self.maximum_path = max(self.maximum_path, new_path_through_root)

        return self.maximum_path


    def max_path_starting_from_root(self, root):

        if root is None:
            return 0
        
        maximum_path_left_child = max(0, self.max_path_starting_from_root(root.left))

        maximum_path_right_child = max(0, self.max_path_starting_from_root(root.right))

        new_path_through_root = maximum_path_left_child + maximum_path_right_child + root.val

        self.maximum_path = max(self.maximum_path, new_path_through_root)

        maximum_path_through_root_and_left = maximum_path_left_child + root.val
        maximum_path_through_root_and_right = maximum_path_right_child + root.val
        
        return maximum_path_through_root_and_left if maximum_path_left_child > maximum_path_right_child else maximum_path_through_root_and_right

