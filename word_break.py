# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        memo = {}

        def dfs(s):

            if s in memo:
                return memo[s]

            for word in wordDict:

                if not s.startswith(word):
                    continue
                
                # we can start with this word
                remainingS = s[len(word):]
                
                # if we find a solution, no need to further search
                if not remainingS:
                    memo[s] = True
                    return True
                # otherwise we move on with the search tree
                elif dfs(remainingS):
                    memo[s] = True
                    return True

                # if we cannot find a solution starting with this word
                # we do nothing and move to the next word
            
            # after exhuasting all words, if we still cannot find a solution
            # return False
            memo[s] = False
            return False

        return dfs(s)