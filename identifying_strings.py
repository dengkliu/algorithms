# https://www.lintcode.com/problem/333/

# Given n character strings containing only lower case letters, 
# find the minimum prefix strings that can identify each string.
# That is, the minimum prefix string Ap which identifies string 
# A will not be a prefix string of other n-1 character strings.

#
#  a -> a -> a
#  b -> b -> b
#  b -> c -> d

# Brute force - For each word, enumerate all prefixes from short to long, and record how many words it map to (with dictioanry)
# Then for each word, check all prefixes from short to long, and return the first prefix that maps to only 1 word
# Time complexity: For each word, there are L prefixes (including the word itslef), and the average length of all prefixes is L/2
# The total time complexity is L^2, as it takes L time to check the prefix key letter by letter in dictionary 

# Use Trie

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.chidren = {}
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root

    def insert(self, word):
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.chidren:
                node.chidren[word[i]] = TrieNode()
            node = node.chidren[word[i]]
            node.prefix_count += 1
        
        node.is_word = True
        node.word = word

class Solution:

    def __init__(self):
        self.trie = Trie()

    #"aaa","bbc","bcd"
    # a -> a -> a
    # b -> b -> c
    #   -> c -> d
    """
    @param stringArray: a string array
    @return: return every strings'short peifix
    """
    def ShortPerfix(self, stringArray):
        for word in stringArray:
            self.trie.insert(word)
        
        result = []

        for word in stringArray:
            self.dfs(word, 0, result, self.trie.get_root(), "")
        
        return result

    def dfs(self, word, index, result, root, prefix):
        
        if root.prefix_count == 1:
            result.append(prefix)
            return

        ## [aa, aaa]
        ## aa will reach end of prefix, while the prefix count is still 2
        if root.is_word and root.word == word:
            result.append(word)
            return
        
        prefix += word[index]

        self.dfs(word, index + 1, result, root.chidren[word[index]], prefix)
