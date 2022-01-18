# https://www.lintcode.com/problem/384/
# Given a string, find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: 3
# Explanation: The longest substring is "abc"

# 典型的不确定range长度的substring问题 用同向双指针解决

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        unique_chars = set([])
        end = 0
        result = 0

        for start in range(len(s)):
            while end < len(s) and s[end] not in unique_chars:
                unique_chars.add(s[end])
                end += 1

            if end == len(s):
                result = max(result, end - start)
                break
            
            result = max(result, end - start)

            unique_chars.remove(s[start])

        return result