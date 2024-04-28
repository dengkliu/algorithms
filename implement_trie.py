# https://leetcode.com/problems/implement-trie-prefix-tree/description/

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
        curr.word = word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(root, word, index):
            if index == len(word):
                return root.is_word
            
            if word[index] in root.children:
                return dfs(root.children[word[index]], word, index + 1)
            else:
                return False

        return dfs(self.root,word, 0)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        def dfs(root, prefix, index):
            if index == len(prefix):
                return True
            
            if prefix[index] in root.children:
                return dfs(root.children[prefix[index]], prefix, index + 1)
            else:
                return False
        
        return dfs(self.root, prefix, 0)