// Alice and Bob work in a beautiful orchard. 
// There are N apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N.
// Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees.
// They want to choose to disjoint segements (one consisting of K trees of Alice and the other consisting of L trees for Bob) so as not to disturb each other. 
// You should return the maximum number of apples that they can collect.

// 典型的fixed size sliding window + 双字段问题
// 双字段问题可以用隔板法。

public class Solution {
    /**
     * @param A: a list of integer
     * @param K: a integer
     * @param L: a integer
     * @return: return the maximum number of apples that they can collect.
     */
    public int PickApples(int[] A, int K, int L) {
        // 隔板法
        int n = A.length;

        int maxApple = Integer.MIN_VALUE;

        for (int i = 0; i < n; i ++) {
            // 1 2 3 4 | 53 6 2
            // 枚举隔板 [0, i) [i, n)

            // 假如K在L左边
            int leftMaxK = getMax(A, K, 0, i);
            int rightMaxL = getMax(A, L, i, n);

            if (leftMaxK != -1 && rightMaxL != -1) {
                maxApple = Math.max(maxApple, leftMaxK + rightMaxL);
            }

            // 假如L在K左边
            int leftMaxL = getMax(A, L, 0, i);
            int rightMaxK = getMax(A, K, i, n);

            if (leftMaxL != -1 && rightMaxK != -1) {
                maxApple = Math.max(maxApple, leftMaxL + rightMaxK);
            }
        }

        if (maxApple == Integer.MIN_VALUE) {
            return -1;
        }

        return maxApple;
    }

    private int getMax(int[] A, int n, int left, int right) {

        // 6 1 4 6 | 6 3 2 7 4
        // left = 0, right = 4 [0, 4) 中间有4个数
        // 假如n > 4 说明长度不够 直接返回 -1 
        if (right - left < n) {
            return -1;
        }

        //初始化
        int sum = 0;
        for (int i = left; i < left + n; i ++) {
            sum += A[i];
        }
        int max = sum;

        // 开始移动
        int start = left;
        int end = start + n;

        while (end < right) {
            sum -= A[start];
            sum += A[end];
            max = Math.max(max, sum);
            start ++;
            end ++;
        }

        return max;
    }
}
