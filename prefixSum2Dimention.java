public class prefixSumTwoDimention {

	// S[i][j] = sum(A[u][v]) where 0 <= u <= i, 0 <= v <= j.
	// 以这个元素为右下角的矩阵的所有元素之和


	// s[i][j] = s[i-1][j] + s[i][j-1] + a[i][j] - s[i-1][j-1]

	// prefixSum from A[x1][y1] to A[x2, y2] = s[x2+1][y2+1] - s[x1][y2+1] - s[x2+1][y1] + s[x1][y1] -- 多减了一次

	int[][] A = [[1, 2, 3], [1, 2, 3]];

	int n = A.length;
	int m = A[0].length;

	int[][] prefixSum = new int[n+1][m+1];

	public void getPrefixSum() {

		for (int i = 1; i < n+1; i ++) {
			for (int j = 1; j < m+1; j ++) {
				prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + A[i-1][j-1];
			}
		}
	}
}