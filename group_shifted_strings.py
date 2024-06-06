# https://leetcode.com/problems/group-shifted-strings/description/

# Perform the following shift operations on a string:

# Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
# Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
# We can keep shifting the string in both directions to form an endless shifting sequence.

# For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
# You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        patterns = collections.defaultdict(list)

        # "abc"
        # 
        for s in strings:
            pattern = []

            if len(s) == 1:
                patterns['0'].append(s)
                continue

            # az ba 
            # z - a + 26 = 25 % 26  25
            # a - b + 26 = -1 % 26  25
            pattern = []
            for c in s:  
                diff = ord(c) - ord(s[0])
                pattern.append(chr(diff % 26))

            patterns[''.join(pattern)].append(s)

        return list(patterns.values())