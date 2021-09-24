# https://www.lintcode.com/problem/1448/

# A card game that gives you the number of cards n，and two non-negative integers: totalProfit, totalCost. 
# Then it will give you the profit value of every card a[i] and the cost value of every card b[i].
# It is possible to select any number of cards from these cards, form a scheme. 
# Now we want to know how many schemes are satisfied that all selected cards' profit 
# values are greater than totalProfit and the costs are less than totalCost.

class Solution:
    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """

    # 技巧 对于这种大于或者小于 转化为大于等于和小于等于 这样方便初始化！！
    # dp[i][j][k] -> 对于i张卡 profit超过或者等于j cost小于或者等于k的total schemas
    # dp[i][j][k] = dp[i-1][j-a[i-1]][k-b[i-1]] + dp[i-1][j][k]
    def numOfPlan(self, n, totalProfit, totalCost, a, b):

        MOD = 10**9 + 7

        # 方便初始化
        totalProfit += 1
        totalCost -= 1

        # python 定义 array 先column 再 row
        dp = [[[0 for c in range(totalCost  + 1)] for r in range(totalProfit + 1)] for k in range(n + 1)]

        # dp[0][0][0] = 1
        # dp[i][0][0] = 1
        # dp[0][i][0] = 0
        # dp[0][0][i] = 1 --> profit超过或者等于0总有一种情况

        # 初始化
        for cost in range(0, totalCost + 1):
               dp[0][0][cost] = 1

        # 从有两张卡开始
        for i in range(1, n + 1):
            for profit in range(0, totalProfit + 1):
                for cost in range(0, totalCost + 1):
                    # 不拿这张卡
                    dp[i][profit][cost] = dp[i-1][profit][cost]
                    # 拿这张卡
                    if cost >= b[i-1]:
                        # 假如这张卡的profit大于当前profit 要拿！
                        prevProfit = max([0, profit - a[i-1]])
                        dp[i][profit][cost] += dp[i-1][prevProfit][cost-b[i-1]]
                        # 先加完最后取模
                        dp[i][profit][cost] %= MOD

        return dp[n][totalProfit][totalCost]


