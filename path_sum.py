# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(root, target):

            # why can't we simply do 
            #  return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)
            if not root:
                return False

            if not root.left and not root.right:
                return root.val == target
            
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)
    
        return dfs(root, targetSum)