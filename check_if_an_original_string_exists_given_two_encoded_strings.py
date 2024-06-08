# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

# An original string, consisting of lowercase English letters, can be encoded by the following steps:

# Arbitrarily split it into a sequence of some number of non-empty substrings.
# Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
# Concatenate the sequence as the encoded string.
# For example, one way to encode an original string "abcdefghijklmnop" might be:

# Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
# Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes ["ab", "12", "1", "p"].
# Concatenate the elements of the sequence to get the encoded string: "ab121p".
# Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

# Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

class Solution(object):

    # s1 = 2b3c s2 = 1b3a
    # step 1: s1 = 1b3c, s2 = b3a --> reduce either matchers cnt to 0
    # step 2: s1 = b3c, s2 = 3a ---> reduce all the chars 
    # step 3: s1 = 3c, s2 = 2a --> reduce either matchers cnt to 0
    # step 4: s1 = 1c, s2 = a. 
    # step 5: s1 = c, s2 = '' --> False

    memo = {}

    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def getNumbers(str):
            ans = set()
            # ["1", "8"]
            # helper(1, "1", 0)
            # helper(2, "18", 0)
            # helper(2, "8", 1)
            # helper(3, "123", 0), helper(3, "3", 12), helper(3, "23", 1), helper(3, "3," 12)
            # 6 24 15 123
            def helper(index, cur_str, cur_sum):
                if index == len(str):
                    ans.add(cur_sum + int(cur_str))
                    return
                # combine the cur_str with new char, so we don't need to update the sum
                helper(index + 1, cur_str + str[index], cur_sum)
                # not combine, start a new number, so we need to update the sum
                helper(index + 1, str[index], cur_sum + int(cur_str))
               
            helper(1, str[0], 0)
            
            return ans

        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        if not s1 and not s2:
            return True

        if not s1 or not s2:
            return False

        if not s1[0].isdigit() and not s2[0].isdigit():
            if s1[0] != s2[0]:
                return False
            res = self.possiblyEquals(s1[1:], s2[1:])
            return res
        elif s1[0].isdigit() and s2[0].isdigit():
            digits1, p1 = s1[0], 1
            while p1 < len(s1) and s1[p1].isdigit():
                digits1 += s1[p1]
                p1 += 1
            digits2, p2 = s2[0], 1
            while p2 < len(s2) and s2[p2].isdigit():
                digits2 += s2[p2]
                p2 += 1
            
            all_possible_nums1 = getNumbers(digits1)
            all_possible_nums2 = getNumbers(digits2)

            for num1 in all_possible_nums1:
                for num2 in all_possible_nums2:
                    res = False
                    if num1 > num2:
                        res = self.possiblyEquals(str(num1-num2) + s1[p1:], s2[p2:])
                        self.memo[(str(num1-num2) + s1[p1:], s2[p2:])] = res
                    elif num2 > num1:
                        res = self.possiblyEquals(s1[p1:], str(num2 - num1) + s2[p2:])
                        self.memo[(s1[p1:], str(num2 - num1) + s2[p2:])] = res                    
                    else:
                        res = self.possiblyEquals(s1[p1:], s2[p2:])     
                        self.memo[(s1[p1:], s2[p2:])] = res  
                    if res:
                        return True
            return False
        else:   
            if s1[0].isdigit():
                s1, s2 = s1, s2  
            else:
                s1, s2 = s2, s1

            digits1, p1 = s1[0], 1
            while p1 < len(s1) and s1[p1].isdigit():
                digits1 += s1[p1]
                p1 += 1
            all_possible_nums1 = getNumbers(digits1)
            for num1 in all_possible_nums1:
                res = False
                if num1 == 1:
                    res = self.possiblyEquals(s1[p1:], s2[1:])
                    self.memo[(s1[p1+1:], s2[1:])] = res       
                else:
                    res = self.possiblyEquals(str(num1 - 1) + s1[p1:], s2[1:])
                    self.memo[(str(num1 - 1) + s1[p1:], s2[1:])] = res
                if res:
                    return True
            
            return False 