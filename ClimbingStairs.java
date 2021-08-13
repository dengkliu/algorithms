// https://www.lintcode.com/problem/111/
// You are climbing a stair case. 
// It takes n steps to reach to the top. 
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Input n = 3
// Output 3
// Explanation:
// 1, 1, 1
// 1, 2
// 2, 1
// total 3.

// Keyword: path, the total number of distinct ways

public class Solution {
    /**
     * @param n: An integer
     * @return: An integer
     */
    public int climbStairs(int n) {

    	if (n==0) {
    		return 0;
    	}
        // What is the state?
        // The total number of distinct ways only depends on the current step
        // dp[i] - the total number of distinct ways to reach step i

        // What is the function for state transition
        // dp[i] = dp[i-1] + dp[i-2]

        // Initialization
        int[] dp = int[n+1];
        dp[0] = 1;

        for (int i = 1; i < n + 1; i ++) {

        	if (i == 1) {
        		dp[i] = dp[i-1];
        		continue;
        	} 

        	dp[i] = dp[i-1] + dp[i-2];
        }

        // What is the result?
        // The total number of distint ways to reach step n
        return dp[n];
    }
}