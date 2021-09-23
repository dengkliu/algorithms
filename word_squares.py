# https://www.lintcode.com/collection/178/

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

class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):

        prefix_to_words = self.get_prefix_to_words(words)

        # 定义储存结果的list
        squares = []

        for word in words:
            self.search(prefix_to_words, [word], squares)

        return squares

    def get_prefix_to_words(self, words) :

        # dictionary
        prefix_to_words = {} 

        for word in words:
            for i in range(len(word)):
                # get first i characters form the word
                prefix = word[0:i + 1]
                # Python dictionary method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
                prefix_to_words.setdefault(prefix, [])
                # 加prefix -> word 关系
                prefix_to_words[prefix].append(word)

        return prefix_to_words

    
    def search(self, prefix_to_words, square, squares):
        square_row_cnt = len(square[0])
        curr_row_cnt = len(square)

        if square_row_cnt == curr_row_cnt:
            # 重要！需要再造一个list 不然这个square会被之后的代码修改
            squares.append(list(square))
            return


        # separator: ''
        # build a list iteratively [ element for element in another list ]    
        prefix = ''.join([square[i][curr_row_cnt] for i in range(curr_row_cnt)])

        # print('prefix: ' + prefix)
        
        for word in prefix_to_words.get(prefix, []):
            square.append(word)
            self.search(prefix_to_words, square, squares)
            # remove last item
            square.pop() 

    
