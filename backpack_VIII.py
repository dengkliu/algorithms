# https://www.lintcode.com/problem/799

# Given coins with different values and quantities, 
# find out how many ways of total values in the range of [1, n] can be formed?

# Example 1:
# 	Input:  
#		n = 5
#		value = [1,4]
#		amount = [2,1]
#	Output:  4
	
#	Explanation:
#	They can combine 4 numbers which are 1,2,4,5.

# dp[i][j] ----> can I form j if I have i values?
# dp[i][0] = 0
# dp[i][j] = dp[i-1][j] and dp[i-1][j-value[i]] (if j >= value[i])
# what if we introduce coin counts here?
# add one more for loop through coin counts
# and the check becomes j >= cnt * value[i]
class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    # dp[i][j] -- given coins with value i, whether number j can be formed
    def backPackVIII(self, n, value, amount):
        # write your code here

        if not value or len(value) == 0:
            return 0

        coin_value_cnt = len(value)

        dp = [[False for _ in range(n + 1)] for _ in range(coin_value_cnt + 1)]

        for i in range(coin_value_cnt):
            dp[i][0] = True

        for i in range(1, coin_value_cnt + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                for coin_cnt in range(1, amount[i - 1] + 1):
                    if (coin_cnt * value[i - 1] <= j):
                        dp[i][j] = dp[i][j] or \
                            dp[i - 1][j - coin_cnt * value[i - 1]]
                            
        total_way = 0

        for i in range(1, n + 1):
            if dp[coin_value_cnt][i]:
                total_way += 1
        
        return total_way