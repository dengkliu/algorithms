// https://www.lintcode.com/problem/89/

// Given n distinct positive integers, integer k (k=n) and a number target.
// Find k numbers where sum is target. Calculate how many solutions there are?

// A = [1,2,3,4]
// k = 2
// target = 5

// 典型的DFS 组合类问题 但是DFS可能会超时 复杂度 C(n, 2)
public class Solution {

    int result = 0;
    /**
     * @param A: An integer array
     * @param k: A positive integer (k <= length(A))
     * @param target: An integer
     * @return: An integer
     */
    public int kSum(int[] A, int k, int target) {
        Arrays.sort(A);
        dfs(0, k, target, A);
        return result;
    }

    void dfs(int index, int k, int target, int[] A) {
        
        if (k == 0 && target == 0) {
            result ++;
            return;
        }

        if (k == 0 || target == 0) {
            return;
        }

        for (int i = index; i < A.length; i ++) {
            dfs(i + 1, k - 1, target - A[i], A);
        }
    }
}

// 经典的DP题 求方案总数 复杂度 n * k * target

public class Solution {

    int result = 0;
    /**
     * @param A: An integer array
     * @param k: A positive integer (k <= length(A))
     * @param target: An integer
     * @return: An integer
     */

    // 背包类DP
    public int kSum(int[] A, int k, int target) {  

        Arrays.sort(A);

        int [][][] dp = new int[A.length + 1][k + 1][target + 1];

        // dp[n][k][sum]
        // 在第n个数时候 1. 一共加了k个数 2. 得到sum ---> 有多少种方案？

        // 加0个数得到0，永远有一个方案
        for (int i = 0; i < A.length + 1; i ++) {
            dp[i][0][0] = 1;
        }

        for (int i = 1; i <= A.length; i ++) {
            // 目前为止考虑了i个数 最多也就能加i个数
            for (int j = 1; j <= k && j <= i; j++) {
                for (int sum = 1; sum <= target; sum ++) {
                    // 能加入这个数的话，就加入
                    if (A[i-1] <= sum) {
                        dp[i][j][sum] += dp[i - 1][j - 1][sum - A[i - 1]];
                    }

                    // 不加入这个数的方案总数
                    dp[i][j][sum] += dp[i-1][j][sum];
                }
            }
        }

        return dp[A.length][k][target];

    }
}