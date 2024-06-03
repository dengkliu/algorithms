# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        stack = []
        index_to_remove = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    index_to_remove.append(i)
                else:
                    stack.pop()
        
        while stack:
            index_to_remove.append(stack.pop())

        letters = []
        for i in range(len(s)):
            if i not in index_to_remove:
                letters.append(s[i])

        return ''.join(letters)