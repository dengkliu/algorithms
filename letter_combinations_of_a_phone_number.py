# https://www.lintcode.com/problem/270/

# Given some digit strings excluded 0 and 1 and a dict, for each digth string return 
# the number of possible letter combinations in dict that the number could match.
# If we can use a digit string represent the prefix of a word, we think they can match.
# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Input: query = ["2", "3", "4"]
# dict = ["a","abc","de","fg"]
# Output:[2,2,0]
# Explanation: 
# "a" "abc" match "2"
# "de" "fg" match "3"
# no word match "4"

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

    # get the word count for a given prefix
    def get_word_count(self, prefix):
        node = self.get_root()
        for letter in prefix:
            if letter not in node.chidren:
                return 0
            node = node.chidren[letter]
        return node.word_count

class Solution:

    def __init__(self):
        self.trie = Trie()
        self.letter_to_digit = {}
        self.letter_to_digit["a"] = "2"
        self.letter_to_digit["b"] = "2"
        self.letter_to_digit["c"] = "2"
        self.letter_to_digit["d"] = "3"
        self.letter_to_digit["e"] = "3"
        self.letter_to_digit["f"] = "3"
        self.letter_to_digit["g"] = "4"
        self.letter_to_digit["h"] = "4"
        self.letter_to_digit["i"] = "4"
        self.letter_to_digit["j"] = "5"
        self.letter_to_digit["k"] = "5"
        self.letter_to_digit["l"] = "5"
        self.letter_to_digit["m"] = "6"
        self.letter_to_digit["n"] = "6"
        self.letter_to_digit["o"] = "6"
        self.letter_to_digit["p"] = "7"
        self.letter_to_digit["q"] = "7"
        self.letter_to_digit["r"] = "7"
        self.letter_to_digit["s"] = "7"
        self.letter_to_digit["t"] = "8"
        self.letter_to_digit["u"] = "8"
        self.letter_to_digit["v"] = "8"
        self.letter_to_digit["w"] = "9"
        self.letter_to_digit["x"] = "9"
        self.letter_to_digit["y"] = "9"
        self.letter_to_digit["z"] = "9"

    """
    @param queries: the queries
    @param dict: the words
    @return: return the queries' answer
    """
    # build a trie, and then for each number, check the total number
    def letterCombinationsII(self, queries, dict):

        for word in dict:
            new_word = ""
            for letter in word:
                digit = self.letter_to_digit[letter]
                new_word += digit
            self.trie.add_word(new_word)

        result = []

        for query in queries:
            result.append(self.trie.get_word_count(query))

        return result