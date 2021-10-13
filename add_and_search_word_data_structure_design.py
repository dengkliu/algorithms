# https://www.lintcode.com/problem/473/

# Design a data structure that supports the following two operations: addWord(word) and search(word)
# Addword (word) adds a word to the data structure.search(word) can search a literal word 
# or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.

# Input:
#  addWord("bad")
#  addWord("dad")
#  addWord("mad")
#  search("pad")  
#  search("bad")  
#  search(".ad")  
#  search("b..")  
# Output:
#  false
#  true
#  true
#  true

# Brute force 用dictionary 每次添加一个word 所有能够匹配到这个word的expression加到dictionary里面去 太多了 1 + C(n, 1) + C(n, 2) + ... + C(n, n)
# 比如 "bad" -> "bad" ".ad" "b.d" "ba." "..d" "b.." ".a." "..." 
# 时间复杂度太高了

# 用Trie 字典树 Retrieve

class TrieNode:
    def __init__(self):
    	# 每个children都是 letter -> node， 这里letter就是一个边
        self.children = {}
        # 很重要 表示这里就是一个完整的单词 之后的search DFS会用到
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                # 新建一个trie node
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
    
        node.is_word = True
        node.word = word
        # write your code here
        
class WordDictionary:

    def __init__(self):
        self.trie = Trie()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.dfs(self.trie.get_root(), word, 0)
    
    def dfs(self, root, word, index):

        if index == len(word):
            # 关键！看看是不是一个单词
            return root.is_word
        
        letter = word[index]
        if letter == '.':
            for child in root.children:
                # 只要有任何一个能找到 就立刻返回true
                if self.dfs(root.children[child], word, index + 1):
                    return True
            return False
        elif letter in root.children:
            return self.dfs(root.children[letter], word, index + 1)
        return False



