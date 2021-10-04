class UnionFind:

	def _init_(self):
		# a dictionary maps from child to fater
		# 初始化父指针
		# 集合大小
		# 集合的数量
		self.father = {}
		self.size_of_set = {}
		self.num_of_set = 0

	def add(self, x):
		if x in self.father:
			return
		# 初始化点的父亲为对象 None
		# 集合数量 +1
		# 初始化节点所在集合大小为 1
		self.father[x] = None
		self.num_of_set += 1
		self.size_of_set[x] = 1

	def merge(self, x, y):

		# 找到两个节点的根
		root_x = self.find(x)
		root_y = self.find(y)

		# 如果根不是同一个，则连接
		if root_x != root_y:
			# 将一个点的根变成新的根
			# 集合的数量减少1
			# 计算新的根所在的集合大小
			self.father[root_x] = root_y
			self.num_of_set -= 1
			self.size_of_set[root_y] += self.size_of_set[root_x]

	# 查找一个x所在的set
	def find(self, x):
		# 指针 root 指向被查找的点
		# by defualt 一个点的父亲是他自己
		root = x
		while self.father[root] != None:
			root = self.father[root]

		# 将从x往上走路径上所有的节点指向根root
		while x!= root:
			# 暂存 x 原本的父亲
			# 将x指向根节点
			# x指针上移到x的父节点
			original_fater = self.father[x]
			self.father[x] = root
			x = original_fater

		return root

	def is_connected(self, x, y):
		return self.find(x) == self.find(y)

	def get_num_of_set(self):
		return self.num_of_set

	def get_size_of_set(self, x):
		return self.size_of_set(self.find(x))

