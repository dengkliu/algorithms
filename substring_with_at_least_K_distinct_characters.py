# https://www.lintcode.com/problem/1375
# Given a string S with only lowercase characters.
# Return the number of substrings that contains at least k distinct characters.

# 10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
# 1 ≤ k ≤ 261≤k≤26

# 1. Brute-force - enumerate all substrings, and count of the number of unique characters. Worst case O(N^3)
# 2. Two pointers - 同向双指针。用Hashmap而不是set 因为hash set只有0和1的区别 hash map才能增加和减少次数

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):

        if not s:
            return 0

        # Write your code here
        letter_cnt = {}

        end = 0
        result = 0

        # "abcabcabcabc"
        #  bca 

        for start in range(len(s)):
            while end < len(s) and len(letter_cnt) < k:
                if s[end] not in letter_cnt:
                    letter_cnt[s[end]] = 1
                else:
                    letter_cnt[s[end]] += 1
                end += 1
                
            if len(letter_cnt) >= k:
                result += (len(s) - 1) - (end - 1) + 1
            else:
                return result
            
            letter_cnt[s[start]] -= 1

            if letter_cnt[s[start]] == 0:
                del letter_cnt[s[start]]
        
        return result 