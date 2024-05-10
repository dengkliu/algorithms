# https://leetcode.com/problems/valid-word-abbreviation/

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        indice1, indice2 = 0, 0

        while indice1 < len(word) and indice2 < len(abbr):
            if word[indice1] == abbr[indice2]:
                indice1 += 1
                indice2 += 1
            else:
                if abbr[indice2].isdigit():
                    num = 0

                    # Corner case: number cannot start 0
                    if int(abbr[indice2]) == 0:
                        return False

                    # Corner case: the last character in abbr is a digit
                    while indice2 < len(abbr) and abbr[indice2].isdigit():
                        num = num * 10 + int(abbr[indice2])
                        indice2 += 1
                    
                    # Why do we want this?
                    # How many chars we have (including this char) until end
                    if len(word) - indice1 < num:
                        return False
                    
                    # Skip all chars in between
                    while num:
                        indice1 += 1
                        num -= 1 

                    continue
                else:
                    return False
        
        # Corner case: there are still characters in one of the string
        if indice1 < len(word) or indice2 < len(abbr):
            return False
        
        return True