// Say you have an array for which the ith element is the price of a given stock on day i.

// If you were only permitted to complete at most one transaction 

// (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

// Input: [3, 2, 3, 1, 2]
// Output: 1
// Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1

// Greedy - buy at the previous minimum prices and try sell at current day
// If more profit, update the result, otherwise hold. 

public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
    
        // 3 2 3 1 2
        // 3 2 2 1 1
        // 0 -1 1 -1 1
        // write your code here
        int minimum = Integer.MAX_VALUE;

        int result = 0;

        for (int i = 0; i < prices.length; i++) {

            // remember previous smallest price
            result = Math.max(result, prices[i] - minimum);

            minimum = Math.min(minimum, prices[i]);
        }

        return result;
    }
}