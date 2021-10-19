# https://www.lintcode.com/problem/1848/

# Given a matrix of lower alphabets and a dictionary. 
# Find maximum number of words in the dictionary that can be found in the matrix in the meantime. 
# A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 
# One character only be used once in the matrix. No same word in dictionary


# Input：
# ["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
# Output：
# 2
# Explanation：
#  d o a f
#  a g a i
#  d c a n
# search in Matrix, you can find `dog` and `can` in the meantime.


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
        self.max_count = 0
        self.DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def wordSearchIII(self, board, words):
        # Edge case
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return 0

        for word in words:
            self.trie.add(word)

        words_found = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                # mark the current as visited
                board[i][j] = '*'
                self.dfs(i, j, i, j, letter, board, words_found, self.trie.get_root())
                board[i][j] = letter
        
        return self.max_count
    
    def dfs(self, x, y, start_x, start_y, current, board, words_found, node):
        
        if current not in node.children:
            return
        
        next_node = node.children[current]
        
        # If we have found a word starting from x and y
        # We move to find word starting from other positions
        if next_node.is_word:

            words_found.append(next_node.word)
            self.max_count = max(self.max_count, len(words_found))
            
            # now let's look for more words
            for i in range(start_x, len(board)):
                if i == start_x:
                    y_min = start_y + 1
                else:
                    y_min = 0
                for j in range(y_min, len(board[0])):
                    next_letter = board[i][j]
                    if next_letter == '*' or next_letter not in next_node.children:
                        continue
                    
                    # mark the next as visited
                    board[i][j] = '*'
                    self.dfs(i, j, i, j, next_letter, board, words_found, next_node)
                    board[i][j] = next_letter
            
            words_found.pop()

        # 不管有没有找一个word，接着继续找
        for dx, dy in self.DIRECTIONS:
            next_x = x + dx
            next_y = y + dy
            
            if not self.validate(next_x, next_y, board):
                continue
            next_letter = board[next_x][next_y]
            if next_letter in next_node.children:
                board[next_x][next_y] = '*'
                self.dfs(next_x, next_y, start_x, start_y, next_letter, board, words_found, next_node)
                board[next_x][next_y] = next_letter

    def validate(self, x, y, board):
        if x < 0 or x >= len(board):
            return False
        if y < 0 or y >= len(board[0]):
            return False
        if board[x][y] == '*':
            return False
        return True
