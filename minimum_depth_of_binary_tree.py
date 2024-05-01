# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):
            # why do we check all possible cases here?
            if not root.left and not root.right:
                return 1
            elif root.left and not root.right:
                return dfs(root.left) + 1
            elif root.right and not root.left:
                return dfs(root.right) + 1
            else:
                return min(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root)