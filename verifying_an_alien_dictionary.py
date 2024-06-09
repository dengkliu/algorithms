# https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letter_order = {}
        for index, letter in enumerate(order):
            letter_order[letter] = index

        # apple app
        for word1, word2 in zip(words, words[1:]):
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    if letter_order[letter1] > letter_order[letter2]:
                        return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True