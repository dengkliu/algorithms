# https://leetcode.com/problems/word-squares/description/

# Given a set of words without duplicates, find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# Input:
# ["area","lead","wall","lady","ball"]
# Output:
# [["wall","area","lead","lady"],["ball","area","lead","lady"]]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# 1. 典型的排列问题。单词的顺序是matter的。暴力解法 - 找到所有排列方式，然后验证是否是对称的。假设有n个单词，每个单词长度为m。
#    所有排列个数 n! 验证每个排列是否是word square m^2 总时间复杂度 n! * m^2
# 2. 怎么优化呢？第n行的word 前n-1个字母一定与第n列的前n-1个字母相同 ---> 前缀 prefix问题！
#    如何快速找到以某个前缀为开头的单词？1. trie, prefix tree 2. hashtable

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        def get_prefix_to_words(words):
            prefix_to_words = collections.defaultdict(list)


            # O(N * L)
            for word in words:
                for i in range(len(word)):
                    prefix = word[0:i + 1]
                    prefix_to_words[prefix].append(word)
            
            return prefix_to_words

        def search(square, squares, prefix_to_words):
            if len(square) == len(square[0]):
                # why do we want to copy the square?
                squares.append(list(square))
                return
            
            cur_row_cnt = len(square)

            # This is for optimization
            for r in range(cur_row_cnt, len(square[0])):
                prefix = ''.join([square[i][r] for i in range(cur_row_cnt)])
                if prefix not in prefix_to_words:
                    return
            
            prefix = ''.join([square[i][cur_row_cnt] for i in range(cur_row_cnt)])

            for word in prefix_to_words[prefix]:
                square.append(word)
                search(square, squares, prefix_to_words)
                square.pop()

        prefix_to_words = get_prefix_to_words(words)
        
        squares = []

        for word in words:
            search([word], squares, prefix_to_words)

        return squares