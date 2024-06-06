# https://leetcode.com/problems/valid-number/

# Given a string s, return whether s is a valid number.

# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:

# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.

# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return False

        seen_digit = seen_exponent = seen_dot = False

        for i, c in enumerate(s): 
            if c in ['-', '+']:
                # - and + should either be at the head
                # or they should be right after e/E
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif c in ['e', 'E']:
                # e/E should not be seen before
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # 4e+
                seen_digit = False
            elif c == '.':
                # cannot have . again if we see 
                #exponent or dot already
                if seen_exponent or seen_dot:
                    return False
                seen_dot = True
            elif c.isdigit():
                seen_digit = True
            else:
                return False

        if not seen_digit:
            return False
        
        return True 