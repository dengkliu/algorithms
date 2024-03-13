# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []

        if not root:
            return result

        def dfs(root):

            if not root.left and not root.right:
                if len(result) == 0:
                    result.append([root.val])
                else:
                    result[0].append(root.val)
                return 0

            l_index = 0
            r_index = 0
            
            if root.left:
                l_index = dfs(root.left)
            if root.right:
                r_index = dfs(root.right)

            current_index = max(l_index, r_index) + 1
            
            if len(result) < current_index + 1:
                result.append([root.val])
            else:
                result[current_index].append(root.val)

            return current_index

        dfs(root)

        return result