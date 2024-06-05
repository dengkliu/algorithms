# https://leetcode.com/problems/custom-sort-string/

# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        letter_to_frequency = collections.defaultdict(int)

        for letter in s:
            letter_to_frequency[letter] += 1
        
        ans = []
        for letter in order:
            if letter in letter_to_frequency:
                for i in range(letter_to_frequency[letter]):
                    ans.append(letter)
        
        for letter, frequency in letter_to_frequency.items():
            if letter not in order:
                for i in range(letter_to_frequency[letter]):
                    ans.append(letter)
        
        return ''.join(ans)