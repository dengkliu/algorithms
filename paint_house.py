# https://www.lintcode.com/problem/515/

# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
# For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... 
# Find the minimum cost to paint all houses.

# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    # dp[i][j] --> the minimum costs painting i houses ending in j color
    # dp[i][j] = min(dp[i-1][other color] + costs[i][j])
    def minCost(self, costs):
        # write your code here
        RED = 0
        BLUE = 1
        GREEN = 2

        dp = [[0 for _ in range(3)] for _ in range(len(costs) + 1)]

        for house in range(1, len(costs) + 1):
            for color in range(3):
                if color == RED:
                    dp[house][color] = min(dp[house-1][BLUE] + costs[house - 1][RED], \
                        dp[house-1][GREEN] +costs[house - 1][RED])
                elif color == BLUE:
                    dp[house][color] = min(dp[house-1][RED] + costs[house - 1][BLUE], \
                        dp[house-1][GREEN] +costs[house - 1][BLUE])
                else:
                    dp[house][color] = min(dp[house-1][BLUE] + costs[house- 1][GREEN], \
                        dp[house-1][RED] +costs[house - 1][GREEN])

        result = float('inf')

        for i in range(3):
            result = min(result, dp[len(costs)][i])

        return result  