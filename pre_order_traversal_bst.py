class Solution:
	def preorder_traversal(self, root):
		if root is None:
			return

		stack = []

		stack.append(root)

		preorder = []

		while stack:
			node = stack.pop()
			preorder.append(node.val)
			if root.left is not None:
				stack.append(root.left)
			if root.right is not None:
				stack.append(root.right)

		return preorder
