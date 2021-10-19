# https://www.lintcode.com/problem/132/

# Given a matrix of lower alphabets and a dictionary. 
# Find all words in the dictionary that can be found in the matrix. 
# A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 
# One character only be used once in one word. No same word in dictionary

# Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
# Output：["again","can","dad","dog"]
# Explanation：
#  d o a f
#  a g a i
#  d c a n
# search in Matrix，so return ["again","can","dad","dog"].

# 单词搜索一般用DFS
# 从方正的每个位置开始 看看能不能走出一个单词 
# 为了优化搜索速度，可以用trie. 
# Trie的形状类似树，可以从第一个字符开始逐渐往下，看看能不能找出一个完整的单词

# Definition of trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_root(self):
        return self.root
    def add(self, word):
        node = self.get_root()
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True
        node.word = word

class Solution:

    def __init__(self):
        self.trie = Trie()
        # List of tuple, 在方阵中移动小技巧
        self.DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here

        if board == None or len(board) == 0:
            return []
        
        for word in words:
            self.trie.add(word)

        result = []

        row_count = len(board)
        col_count = len(board[0])

        # (M * N) ^ 2 
        for i in range(row_count):
            for j in range(col_count):
                letter = board[i][j]
                board[i][j] = '*'
                self.dfs(i, j, letter, board, self.trie.get_root(), result)
                board[i][j] = letter
        return result

    def dfs(self, row, col, current, board, node, result):

        if current not in node.children:
            return
    
        if node.children[current].is_word:
            if node.children[current].word not in result:
                result.append(node.children[current].word)

        for dx, dy in self.DIRECTIONS:
            next_row = row + dx
            next_col = col + dy

            if not self.valid(next_row, next_col, board):
                continue
            
            next_letter = board[next_row][next_col]
            board[next_row][next_col] = '*'
            self.dfs(next_row, next_col, next_letter, board, node.children[current], result)
            board[next_row][next_col] = next_letter

    def valid(self, row, col, board):
        if row < 0 or row >= len(board):
            return False
        if col < 0 or col >= len(board[0]):
            return False
        if board[row][col] == '*':
            return False
        return True

