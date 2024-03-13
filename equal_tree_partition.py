# https://www.lintcode.com/problem/864
# Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees 
# which have the equal sum of values after removing exactly one edge on the original tree.

# The range of tree node value is in the range of [-100000, 100000]. --> which means the sum could be 0
# 1 <= n <= 10000
# You can assume that the tree is not null

# 典型的DFS问题 一个🌲的sum == 左子树sum + 右子树sum

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):

        sum_count = {}

        total_tree_sum = self.get_tree_sum(root, sum_count)

        if total_tree_sum == 0:
            return sum_count[0] > 1
        else:
            return total_tree_sum % 2 == 0 and (total_tree_sum / 2) in sum_count 

    def get_tree_sum(self, root, sum_count):
        if root is None:
            return 0
        
        left_sum = self.get_tree_sum(root.left, sum_count)
        right_sum = self.get_tree_sum(root.right, sum_count)
        new_sum = left_sum + right_sum + root.val

        if new_sum not in sum_count:
            sum_count[new_sum] = 0
        sum_count[new_sum] +=1

        return new_sum
