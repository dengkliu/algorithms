# https://www.lintcode.com/problem/194/

# Given a string str and a dictionary dict, you need to find out which words in the dictionary are subsequences of the string and return those words.
# The order of the words returned should be the same as the order in the dictionary.

# |str|<=1000
# the sum of all words length in dictionary<=1000


# Input:
# str="bcogtadsjofisdhklasdj"
# dict=["book","code","tag"]
# Output:
# ["book"]
# Explanation:Only book is a subsequence of str

# 1. Brute force - two pointer
#    For each word, put a pointer at the head of the word, and another pointer at the head of the str
#    if the current character of the word is the same as the character in the str, then move both pointers to next character
#    otherwise just move the pointer for the str
#    Worst case: "abbaa" ["aaa", "aa", ....,] O(N*M) N - string length M - total number of words in the array
# 2. Use hash table to record the index for each character, so we avoid scanning the str
#    Each character may appear in multiple positions, so you need a list.
#    When scanning the word from the dictionary, you can do binary search to speed up further (find out whether there exists a number in the array
#    larger than target number)

class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def findWords(self, str, dict):
        # write your code here.
        
        # build a dictionary, key is the letter, value is an array of letter's position
        letter_positions = self.build_letter_positions(str)

        result = []

        for word in dict:
            # check if word is a subsequence of the string
            if self.isValid(word, letter_positions):
                result.append(word)
        
        return result

    def build_letter_positions(self, str):
        letter_positions = {}

        for i in range(len(str)):
            letter = str[i]

            if letter in letter_positions:
                letter_positions[letter].append(i)
            else:
                letter_positions[letter] = []
                letter_positions[letter].append(i)
        
        return letter_positions

    def isValid(self, word, letter_positions):
        # for each word in the dict, check each letter one by one and identify the position
        # for example, for the first letter, always find the first position in the string
        # for the second letter, then we need to find the first position that is larger 
        # than the position of the first letter.
        # So the problem is reduced to -- given a target number, 
        # find the least number larger than the target. 
        prev_position = -1
        for letter in word:
            prev_position = self.find_position(letter, prev_position, letter_positions) 
            if prev_position == -1:
                return False
        
        return True
    
    def find_position(self, letter, prev_position, letter_positions):

        print(prev_position)
        print(letter)

        if letter not in letter_positions:
            return -1
        
        positions = letter_positions[letter]

        start, end = 0, len(positions) - 1

        while start + 1 < end:
            mid = (start + end)//2
            if positions[mid] > prev_position:
                end = mid
            elif positions[mid] == prev_position:
                start = mid
            else:
                start = mid
        
        if positions[start] > prev_position:
            return positions[start]
        if positions[end] > prev_position:
            return positions[end]
        
        return -1
