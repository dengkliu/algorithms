# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:

	def inorder_traversal(self, root):
		if root is None:
			return

		dummy = TreeNode(0)
		dummy.right = root

		stack = []
		stack.append(dummy)

		inorder = []

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
