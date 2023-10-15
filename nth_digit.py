# https://leetcode.com/problems/nth-digit/description/
# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]

# Problem that involved digits and number conversion 

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start len  digit_count
        # 1.    1.   9 * len
        # 10.   2.   90 * len
        # 100.  3.   900 * len
        # 9 * 10^(n-1) * n

        if n < 9:
            return n
        
        base = 9
        digits = 1
        while n > base * digits:
            n = n - base * digits
            base = base * 10
            digits = digits + 1

        # 1 2 3 4 5 6 7 8 9 10
        # n = 11  11-9=2 
        # 这个地方 多出来的digits 通过转换 1和2应该指向同一个位置 3和4应该指向同一个位置 得用 (n-1)//digits
        num = 10 ** (digits - 1) + (n-1)//digits 
        index = (n-1)%digits

        return int(str(num)[index])
