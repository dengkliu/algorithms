# https://leetcode.com/problems/minimum-window-substring/

# Given two strings source and target. 
# Return the minimum substring of source which contains each char of target.

# If there is no answer, return "".
# You are guaranteed that the answer is unique.
# target may contain duplicate char, while the answer need to contain at least the same number of that char.
# 0 <= len(source) <= 1000000
# 0<=len(target)<=100000

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        c_to_fre_t = {}

        for c in t:
            if c not in c_to_fre_t:
                c_to_fre_t[c] = 0
            c_to_fre_t[c] += 1
        
        end = 0
        
        result = ""
        min_len = float('inf')
        num_c_covered = 0
        c_to_fre_s = {}

        # enumerate the start, what's the minimum substring which meets the criteria
        for start in range(len(s)):
            while end < len(s) and num_c_covered < len(c_to_fre_t.keys()):
                c = s[end]

                if c not in c_to_fre_t:
                    end += 1
                    continue

                if c not in c_to_fre_s:
                    c_to_fre_s[c] = 0
                c_to_fre_s[c] += 1

                if c_to_fre_s[c] == c_to_fre_t[c]:
                    num_c_covered += 1
                
                end += 1
            
            if num_c_covered == len(c_to_fre_t.keys()):
                # why end - start not end - start + 1?
                if end - start < min_len:
                    result = s[start : end]
                    min_len = end - start
            
            # why do we have this?
            if end == len(s) and num_c_covered < len(c_to_fre_t.keys()):
                return result
            
            if s[start] in c_to_fre_t:
                if c_to_fre_s[s[start]] == c_to_fre_t[s[start]]:
                    num_c_covered -= 1
                c_to_fre_s[s[start]] -= 1

        return result