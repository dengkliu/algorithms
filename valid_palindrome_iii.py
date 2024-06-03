# https://leetcode.com/problems/valid-palindrome-iii/

# Given a string s and an integer k, return true if s is a k-palindrome.

# A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.


class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        memo = {}  

        def dfs(s, low, high):
            
            if low == high:
                return 0

            if low == high - 1:
                return 0 if s[low] == s[high] else 1

            if (low, high) in memo:
                return memo[(low, high)]

            if s[low] == s[high]:
                memo[(low, high)] = dfs(s, low + 1, high - 1)
            else:
                memo[(low, high)] = 1 + min(dfs(s, low + 1, high), dfs(s, low, high - 1))

            return memo[(low, high)]

        return dfs(s, 0, len(s) - 1) <= k
