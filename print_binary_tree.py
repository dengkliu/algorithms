# https://leetcode.com/problems/print-binary-tree/submissions/

# Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

# The height of the tree is height and the number of rows m should be equal to height + 1.
# The number of columns n should be equal to 2height+1 - 1.
# Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
# Return the constructed matrix res.

# Input: root = [1,2]
# Output: 
# [["","1",""],
# ["2","",""]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        
        def getTreeDepth(root):
            
            if not root:
                return 0
            
            l = getTreeDepth(root.left)
            r = getTreeDepth(root.right)

            return max(l, r) + 1

        height = getTreeDepth(root) - 1
        # row count
        m = height + 1
        # col count
        n = pow(2, m) - 1
        result = [[''] * n for _ in range(m)]

        def dfs(node, row, col):
            if not node:
                return
            result[row][col] = str(node.val)
            dfs(node.left, row + 1, col - pow(2, height - row - 1))
            dfs(node.right, row + 1, col + pow(2, height - row - 1))

        dfs(root, 0, (n - 1)/2)

        return result