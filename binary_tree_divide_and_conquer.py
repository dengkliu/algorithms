
class Solution:
	def divide_conquer(root):

		# 递归出口
		# 一般是看这颗树是不是null就行了
		if root is None:
			return

		left_result = divide_conquer(root.left)

		right_result = divide_conquer(root.right)

		result = merge left_result and right_result

		return result