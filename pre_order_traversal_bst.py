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
			stack.append(root.left)
			stack.append(root.right)

		return preorder