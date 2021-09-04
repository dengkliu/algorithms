// https://www.lintcode.com/problem/151/

// Say you have an array for which the ith element is the price of a given stock on day i.

// Input : [4,4,6,1,1,4,2,5]
// Output : 6

// Design an algorithm to find the maximum profit. You may complete at most two transactions.


public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        
        // 1. 影响最大利润的因素是什么？-- 交易到了第几天 和 交易次数
        // 2. 这两个因素都要放在数组中去，那么状态是什么
        //    dp[i][j] --> 在第j天，最多交易了i次的时候，获得的最大利润
        //    选择：1. 在第j天不卖出 2. 在第j天卖出
        //    1.在第j天不卖出，第j天的最大利润和j-1天的最大利润相等
        //    2.在第j天卖出，第j天的最大利润是两天价格差 + 最多交易j-1次第m天的最大获利 m从0到j-1
        //    dp[i][j] = Math.max(dp[i][j-1], Math.max(dp[i-1][m] + prices[j] - prices[m]))
        if (prices == null || prices.length == 0) {
            return 0;
        }

        int K = 2;

        int[][] dp = new int[K+1][prices.length];

        for (int i = 1; i < dp.length; i++) {
            // maxDiff - 最多交易 i - 1 次时，从第0天到第j-1天最大利润 - 当天价值
            // 在第一天先买入
            int maxDiff = - prices[0];
            for (int j = 1; j < dp[0].length; j++) {
                // 在第j天买入，所以先减去当天价值
                maxDiff = Math.max(maxDiff, dp[i-1][j-1] - prices[j]);
                // 在第j天不卖出 -- dp[i][j-1]
                // 在第j天卖出 -- prices[j] + maxDiff;
                dp[i][j] = Math.max(dp[i][j-1], prices[j] + maxDiff);
            }
        }

        return dp[2][prices.length -1];
    }
}