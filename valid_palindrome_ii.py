# https://leetcode.com/problems/valid-palindrome-ii/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_palindrome(s, low, high):
            sub_s = s[low:high+1]
            return sub_s == sub_s[::-1]
        
        low, high = 0, len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return check_palindrome(s, low, high - 1) or check_palindrome(s, low + 1, high)
            low += 1
            high -= 1
        
        return True

