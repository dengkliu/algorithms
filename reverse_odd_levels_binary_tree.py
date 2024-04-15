# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return
        
        self._dfs(root.left, root.right, 1)

        return root
    
    def _dfs(self, node1, node2, level):

        if node1 is None or node2 is None:
            return

        if level%2 != 0:
            temp = node1.val
            node1.val = node2.val
            node2.val = temp

        self._dfs(node1.left, node2.right, level + 1)
        self._dfs(node1.right, node2.left, level + 1)