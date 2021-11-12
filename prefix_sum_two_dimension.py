class PrefixSum2D: 

	# S[i][j] = sum(A[u][v]) where 0 <= u <= i, 0 <= v <= j.
	# 以这个元素为右下角的矩阵的所有元素之和


	# s[i][j] = s[i-1][j] + s[i][j-1] + a[i][j] - s[i-1][j-1]

	# prefixSum from A[x1][y1] to A[x2, y2] = s[x2+1][y2+1] - s[x1][y2+1] - s[x2+1][y1] + s[x1][y1] -- 多减了一次

	self.A = [[1, 2, 3], [1, 2, 3]]

	def getPrefixSum(self):
		n = len(self.A)
		m = len(self.A[0])
		
		prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
		
		for i in range(1, n+1):
			for j in range(1, m+1):
				prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + A[i-1][j-1];
				
