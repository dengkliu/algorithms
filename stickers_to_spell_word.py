# https://leetcode.com/problems/stickers-to-spell-word/description/

# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        c_fre_in_stickers = []

        # stickers - [with, example, science]
        # target - thehat    
        # [{t->1, h->1}, {e->1, a->1}, {e->2}]
        for sticker in stickers:
            c_fre = collections.defaultdict(int)
            for c in sticker:
                if c in target:
                    c_fre[c] += 1
            c_fre_in_stickers.append(c_fre)

        memo = {} # key = subseq of the target, value = the min # of stickers needed to form the subseq

        def dfs(t):

            if t in memo:
                return memo[t]

            min_stickers_needed = float('inf')

            for c_fre in c_fre_in_stickers:
                used_cnt = 0
                
                 # find the stickers to start with 
                if t[0] not in c_fre:
                    continue

                # we can start with this sticker
                # we have used this sticker
                used_cnt += 1

                # perform a deep copy of the sticker
                # simply beacuse we want to use all the available chars from it
                # but if we go deeper in the search tree, we don't want the sticker to be impacted
                # because we can reuse stickers and there is infinite quantities of each sticker
                c_fre_deep_copy = copy.deepcopy(c_fre)
                # exhaust all the characters that we can use in the sticker
                
                # we maintain what's the remaining chars after we use this sticker
                remainT = []
                for c in t:
                    if c in c_fre_deep_copy and c_fre_deep_copy[c] > 0:
                        c_fre_deep_copy[c] -= 1
                    else:
                        remainT.append(c)
                
                # if we do have remaining sub sequence, we go deeper in the search tree
                # start with all stickers again, and add the result to used_cnt
                if remainT:   
                    # we could have float('inf') returned, but for Python is OK                      
                    used_cnt += dfs(''.join(remainT))
                
                # see if have found a new minimum number of stickers needed 
                # by choosing a different starting sticker
                min_stickers_needed = min(min_stickers_needed, used_cnt)
            
            # cache the minimum number of stickers needed for this subsequence
            memo[t] = min_stickers_needed                       
            return min_stickers_needed

        res = dfs(target)

        return res if res != float('inf') else -1