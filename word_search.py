# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    
        if not word:
            return False

        n = len(board)
        m = len(board[0])

        DIRECTIONS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(r, c, board, n, m, index, word):
            letter = board[r][c]
            if letter != word[index]:
                return False
            index = index + 1
            if index == len(word):
                return True
            board[r][c] = "*"
            for r_d, c_d in DIRECTIONS:
                r_n = r + r_d
                c_n = c + c_d
                if r_n in range(n) and c_n in range(m):
                    if dfs(r_n, c_n, board, n, m, index, word):
                        return True
            board[r][c] = letter

        for r in range(n):
            for c in range(m):
                if dfs(r, c, board, n, m, 0, word):
                    return True

        return False