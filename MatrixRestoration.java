// https://www.lintcode.com/problem/1840/

// There is a matrix before with n rows and m columns.
// For each element in before before[i][j], we will use the following algorithm to convert it to after[i][j]. 
// Given the after matrix, please restore the original matrix before.

// s = 0
// for i1: 0 -> i
//     for j1: 0 -> j
//         s = s + before[i1][j1]
// after[i][j] = s

// Input: 2, 2, [[1,3],[4,10]]
// Output: [[1,2],[3,4]]

// 这道题就是考二维的prefix sum

public class Solution {
    /**
     * @param n: the row of the matrix
     * @param m: the column of the matrix
     * @param after: the matrix
     * @return: restore the matrix
     */

    // prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + A[i][j]
    public int[][] matrixRestoration(int n, int m, int[][] after) {
        // write your code here

        int[][] before = new int[n][m];

        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {

                if (i == 0 && j == 0) {
                    before[i][j] = after[i][j];
                    continue;
                }

                if (i == 0) {
                    before[i][j] = after[i][j] - after[i][j-1];
                    continue;
                }

                if (j == 0) {
                    before[i][j] = after[i][j] - after[i-1][j];
                    continue;
                }

                before[i][j] = after[i][j] - after[i-1][j] - after[i][j-1] + after[i-1][j-1];      
            }
        }

        return before;
    }
}
