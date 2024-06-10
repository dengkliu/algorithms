# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def count_nodes(root):
            if not root:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)

        total_nodes_cnt = count_nodes(root)

        def dfs(root, index, total_nodes_cnt):
            if not root:
                return True
            
            if index >= total_nodes_cnt:
                return False

            return dfs(root.left, 2 * index + 1, total_nodes_cnt) and \
               dfs(root.right, 2 * index + 2, total_nodes_cnt)
        
        return dfs(root, 0, total_nodes_cnt)
