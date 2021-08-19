// https://www.lintcode.com/problem/77

// Given two strings, find the longest common subsequence (LCS).

// Your code should return the length of LCS.

// The longest common subsequence problem is to find the longest common subsequence in a set of sequences (usually 2). This problem is a typical computer science problem, 
// which is the basis of file difference comparison program, and also has applications in bioinformatics.

// Input:

// A = "ABCD"
// B = "EDCA"
// Output:

// 1

// 双序列前缀型动态规划 O(N*M)

// 状态 - dp[i][j] The longest common subsequence of the first i chars in A and first j chars in B
// 初始化 - dp[0][i] = 0 dp[i][0] = 0
// 转移方程 - if A.charAt(i - 1) == B.charAt(j-1) then dp[i][j] = 1 + dp[i-1][j-1]; 
//           else  dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
// 答案  dp[A.length()][B.length()]
public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: The length of longest common subsequence of A and B
     */
    public int longestCommonSubsequence(String A, String B) {

        int lengthOfA = A.length();
        int lengthOfB = B.length();

        // dp[i][j] The longest common subsequence of the first i chars in A and first j chars in B
        int[][] dp = new int[lengthOfA + 1][lengthOfB + 1]; 

        // Initialization, default value is 0, so don't need to redo it here
        // for (int i = 0; i < lengthOfA; i++) {
        //     dp[i][0] = 0;
        // }
        // for (int i = 0; i < lengthOfB; i++) {
        //     dp[0][i] = 0;
        // }

        for (int i = 1; i <= lengthOfA; i++) {
            for(int j = 1; j <= lengthOfB; j++) {
                
                if (A.charAt(i - 1) == B.charAt(j-1)) {
                    dp[i][j] = 1 + dp[i-1][j-1];
                    continue;
                }
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        return dp[lengthOfA][lengthOfB];
    }
}