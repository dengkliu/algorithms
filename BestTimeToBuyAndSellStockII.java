// https://www.lintcode.com/problem/150/

// Given an array prices, which represents the price of a stock in each day.

// You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 

// However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

// Design an algorithm to find the maximum profit.

public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {

        int minimum = Integer.MAX_VALUE;

        int result = 0;

        for (int i = 0; i < prices.length; i ++) {

            if (prices[i] - minimum > 0) {
                // 只要有收益 就卖出
                result += prices[i] - minimum;
                // 最小值更新为当前值，而不是Integer.MAX_VALUE
                // 因为这一天也可以买入而不是必须等到下一天
                minimum = prices[i];
            } else {
                minimum = Math.min(minimum, prices[i]);
            }
        }

        return result;
    }
}
