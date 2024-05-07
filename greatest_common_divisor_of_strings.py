# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        if str1 + str2 != str2 + str1:
            return ""
        
        max_gcd_length = gcd(len(str1), len(str2))

        return str1[:max_gcd_length]