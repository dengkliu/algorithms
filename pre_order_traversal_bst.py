#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
	    return []

        result = []

	# we need a helper function because we want to keep updating result
	# the current method doesn't take the result array as input
        self.preorder(root, result)

        return result
    
    def preorder(self, node, result):
        result.append(node.val)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)

    def preorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
	    return []

	# python implement stack with list
        stack = []
        
        stack.append(root)
        
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
	    # push right first, because left subtree should be traversed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result

