# https://leetcode.com/problems/string-to-integer-atoi/description/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        sign = 1
        total = 0

        if not s:
            return 0

        while index < len(s) and s[index] == " ":
            index += 1

        if index < len(s) and (s[index] == "-" or s[index] == "+"):
            sign = -1 if s[index] == "-" else 1
            index += 1

        while index < len(s):
            # The ord() function returns the number 
            # representing the unicode code of a specified character.
            cur_num = ord(s[index]) - ord("0")
            if cur_num < 0 or cur_num > 9:
                break           
            total = total * 10 + cur_num
            index += 1

        result = total * sign
        
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1 
        
        if result < -pow(2, 31):
            return -pow(2, 31) 
        
        return result