# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversalRecursive(self, root):
        if root is None:
            return []
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root.left:
            self.inorder(root.left, result)
        result.append(root.val)
        if root.right:
            self.inorder(root.right, result)
		
    def inorderTraversalIterative(self, root):
        if root is None:
            return

	stack = []
	dummy = TreeNode(0)
	dummy.right = root
	stack.append(dummy)
	
	result = []
	
	while stack:
		node = stack.pop()
		# for the node popped out, we should look at its right child
		# as in inorder traversal, right child is after the root
		if node.right:
			node = node.right
			stack.append(node)
			
			# but for each node added to the stack, we should look at its left child first
			while node.left:
				node = node.left
				stack.append(node)
				
		if stack:
			inorder.append(stack[-1])

	return inorder
	    
