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