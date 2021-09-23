# A non-negative numbers can be regarded as product of its factors.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Input: 8
# Output: [[2,2,2],[2,4]]
# Explanation:
# 8 = 2 x 2 x 2 = 2 x 4

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        result = []
        # 1. result --> to hold result
        # 2. item --> each combination
        # 3. n --> the current number 
        # 4. start --> this is very important! Only look for larger numbers than this, otherwise there will be duplicates
        self.dfs(result, [], n, 2)
        return result

    def dfs(self, result, item, n, start):

        if (len(item)):
            # 只要找到一个因子，和前一个因子就能成为一个组合，加进去
            item.append(n)
            result.append(list(item))
            # 把这个因子去掉
            item.pop()

        # 对于这个因子, 找到所有的因子组合
        for i in range(start, math.floor(math.sqrt(n) + 1)) :
            if n % i == 0:
                item.append(i)
                self.dfs(result, item, int(n/i), i)
                item.pop()