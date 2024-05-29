# https://leetcode.com/problems/word-search-ii/

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
# Output：["again","can","dad","dog"]
# Explanation：
#  d o a f
#  a g a i
#  d c a n
# search in Matrix，so return ["again","can","dad","dog"].

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        if not words or len(words) == 0 or len(words[0]) == 0:
            return []

        # smart and fast way to build trie!
        trie = {}
        WORD_KEY = "$"
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        n = len(board)
        m = len(board[0])

        DIRECTIONS = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        result = []

        def dfs(r, c, result, board, n, m, parent):
            letter = board[r][c]
            
            if letter not in parent:
                return
            node = parent[letter]

            # why do we need this?
            # to optimize performance, early stop the search
            if not node:
                parent.pop(letter)
                return

            # why do we want to do this?
            # to de-deduplicate
            word_match = node.pop(WORD_KEY, False)
            if word_match:
                result.append(word_match)
            
            board[r][c] = "*"
            for r_d, c_d in DIRECTIONS:
                r_n = r + r_d
                c_n = c + c_d
                if r_n in range(n) and c_n in range(m):
                    dfs(r_n, c_n, result, board, n, m, node)
            board[r][c] = letter

        for r in range(n):
            for c in range(m):
                dfs(r, c, result, board, n, m, trie)

        return result
