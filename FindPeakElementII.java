// https://www.lintcode.com/problem/390

// Given an integer matrix A which has the following features :
// The numbers in adjacent positions are different.
// The matrix has n rows and m columns, n and m will not less than 3.
// For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
// For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]

// We define a position [i, j] is a peak if:
// A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] && 
// A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]

// Input: 
//    [
//      [1, 2, 3, 6,  5],
//      [16,41,23,22, 6],
//      [15,17,24,21, 7],
//      [14,18,19,20,10],
//      [13,14,11,10, 9]
//    ]
// Output: [1,1]
// Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.

// Binary search can be used to find a local minimum or maximum.
// A local minimum or maximum means it is smaller or larger than its neighbor

public class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {

        if (A == null || A.length == 0) {
            return null;
        }

        List<Integer> result = new ArrayList<>();
    
        int rowCnt = A.length;
        int colCnt = A[0].length;

        for (int row = 1; row < rowCnt - 1; row ++) {

            int col = find(row, A);

            if (A[row][col] > A[row - 1][col] && A[row][col] > A[row + 1][col]) {
                result.add(row);
                result.add(col);
                return result;
            }
        }

        return result;
    }

    int find(int row, int[][] A) {

        int start = 1;
        int end = A[0].length - 1;

        while (start + 1 < end) {

            int mid = start + (end - start)/2;

            if (A[row][mid] > A[row][mid - 1]) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return A[row][start] > A[row][end] ? start : end;
    }
}