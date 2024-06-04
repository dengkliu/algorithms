# https://leetcode.com/problems/basic-calculator-ii/description/

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        stack = []
        cur_num = 0
        curr_operation = '+'
        index = 0

        while index < len(s):
            letter = s[index]
            if letter.isdigit():
                cur_num = int(letter)
                index = index + 1
                while index < len(s) and s[index].isdigit():
                    cur_num = cur_num * 10 + int(s[index])
                    index = index + 1
                if curr_operation == '+':
                    stack.append(cur_num)
                elif curr_operation == '-':
                    stack.append(-cur_num)
                elif curr_operation == '*':
                    prev_num = stack.pop()
                    stack.append(prev_num * cur_num)
                elif curr_operation == '/':
                    prev_num = stack.pop()
                    # why do we need this?
                    if prev_num < 0 and prev_num % cur_num != 0:
                        stack.append(prev_num // cur_num + 1)
                    else:
                        stack.append(prev_num // cur_num)

            elif letter.isspace():
                index += 1
            else:
                curr_operation = letter
                index += 1
            
        result = 0

        while stack:
            result += stack.pop()

        return result
        