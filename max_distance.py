# https://www.lintcode.com/problem/1624/

# The distance between the two binary strings is the sum of the lengths of the common prefix removed. 
# For example: the common prefix of 1011000 and 1011110 is 1011, distance is len ("000" + "110") = 3 + 3 = 6. 
# Now give a list of binary strings, find max distance.

# Input：["011000","0111010","01101010"]
# Output：9
# Explanation：the the common prefix of "0111010" and "01101010" is "011", distance is len("1010")+len("01010")=9


# Trie + longest distance between 2 nodes
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        # from letter to next node
        self.chidren = {}
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_root(self):
        return self.root
    def add_word(self, word):
        node = self.get_root()
        for letter in word:
            if letter not in node.chidren:
                node.chidren[letter] = TrieNode()
            node = node.chidren[letter]
            node.word_count += 1
        node.is_word = True
        node.word = word

class Solution:

    def __init__(self):
        self.trie = Trie()
        self.max_distance = 0
        
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def getAns(self, s):
        for word in s:
            self.trie.add_word(word)
        self.dfs(self.trie.get_root())
        return self.max_distance
    
    def dfs(self, node):
        height = 0
        height_zero = 0
        height_one = 0

        if '0' in node.chidren:
            height_zero = self.dfs(node.chidren['0'])
        if '1' in node.chidren:
            height_one = self.dfs(node.chidren['1'])

        # 假如root只有一边的话 不能算进去
        if not (node == self.trie.get_root() and len(node.chidren) < 2):
            self.max_distance = max(self.max_distance, height_zero + height_one)

        return max(height_zero, height_one) + 1