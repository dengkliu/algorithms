# https://www.lintcode.com/problem/1691/

# Given a stock n-day price, you can only trade at most once a day, 
# you can choose to buy a stock or sell a stock or give up the trade today, 
# output the maximum profit can be achieved.

# You can engage in mulitple transactions at the same time

# Given `a = [1,2,10,9]`, return `16`
# Input:
# [1,2,10,9]
# Output:
# 16 -- buy 1, buy 2, sell at 10, sell at 9

# The difference between this problem and problem II is that, you can buy at the second day!!!
# So you have 2 transactions at hand at the same time
# How to achieve this?
# In addition to the solution of problem II (hold the stock when there is a gain)
# you also want to buy at any given time, check if later you can sell it at higher price
# Each time you sell, you are selling the previous minimum.
# You need a data structure to store and update the minimum - priority queue

import heapq

class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def getAns(self, a):
        # write your code here
        heap = []
        ans = 0
        for i in a:
            if heap and i > heap[0]:
            	# the stock price increases, you are holding it, replace with the current price
                ans += i - heapq.heappop(heap)
                heapq.heappush(heap, i)
            # !!!! Important, you can buy another share of current stock
            heapq.heappush(heap,i)
        return ans
