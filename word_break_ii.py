# https://leetcode.com/problems/word-break-ii/description/

# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        memo = {}
        sentenses = []

        # sentences ["cats and dog"]
        # cur_sentences [cat, sand, dog]

        def dfs(s, cur_sentences):

            for word in wordDict:

                if not s.startswith(word):
                    continue
                
                cur_sentences.append(word)

                remainingS = s[len(word):]
                if not remainingS:
                    sentenses.append(' '.join(cur_sentences))
                else:
                    dfs(remainingS, cur_sentences)

                # backtrack - remove the word from cur_sentences
                cur_sentences.pop()

        dfs(s, []) 

        return sentenses