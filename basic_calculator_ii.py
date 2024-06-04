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
        index = 0
        cur_operation = '+'
        cur_num = 0

        while index < len(s):
            if s[index].isspace():
                index += 1
            elif s[index].isdigit():
                cur_num = int(s[index])
                index += 1
                while index < len(s) and s[index].isdigit():
                    cur_num = cur_num * 10 + int(s[index])
                    index += 1 
                if cur_operation == '+':
                    stack.append(cur_num)
                else:
                    stack.append(-cur_num)            
            elif s[index] == '+' or s[index] == '-':
                cur_operation = s[index]
                index += 1
            elif s[index] == '(':
                stack.append(cur_operation)
                cur_operation = '+'
                index += 1
            elif s[index] == ')':
                new_num = 0
                while isinstance(stack[-1], int):
                    new_num += stack.pop()
                operation = stack.pop()
                if operation == '+':
                    stack.append(new_num)
                else:
                    stack.append(-new_num)
                index += 1
        
        result = 0

        while stack:
            result += stack.pop()

        return result