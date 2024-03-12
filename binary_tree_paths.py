# https://leetcode.com/problems/binary-tree-paths/

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        
        def dfs(path, root):
            if not root:
                return

            new_path = ""

            if path == "":
                new_path = str(root.val)
            else:
                new_path = path + "->" + str(root.val)
            
            if not root.right and not root.left:
                result.append(new_path)
                return

            dfs(new_path, root.left)
            dfs(new_path, root.right)

        dfs("", root)

        return result