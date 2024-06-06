# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # 2 ^ 10 = (2 * 2) ^ 5
        # 2 ^ 11 = 2 * (2 * 2) ^ 5

        def binaryPow(x, n):
            if n == 0:
                return 1
            
            if n < 0:
                return 1 / binaryPow(x, -n)

            if n % 2 == 0:
                return binaryPow(x * x, n / 2)
            else:
                return x * binaryPow(x * x, n // 2)

        return binaryPow(x, n)