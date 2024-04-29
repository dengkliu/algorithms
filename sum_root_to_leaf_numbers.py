# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []

        def dfs(root, val):
            # We have to do top down, why?
            curr_val = val * 10 + root.val
            
            if not root.left and not root.right:
                result.append(curr_val)
                
            if root.left:
                dfs(root.left, curr_val)
            if root.right:
                dfs(root.right, curr_val)   

        dfs(root, 0)         
            
        return sum(result)