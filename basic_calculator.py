# https://leetcode.com/problems/basic-calculator/description/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

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
        result = 0
        sign = 1
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
            elif s[index] == '+':
                # First complete the calculation before this operator
                result += sign * cur_num
                sign = 1
                cur_num = 0
                index += 1
            elif s[index] == '-':
                # First complete the calculation before this operator
                result += sign * cur_num
                sign = -1
                cur_num = 0
                index += 1
            elif s[index] == '(':
                # push the result and sign on to the stack, for later
                stack.append(result)
                stack.append(sign)
                # reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                result = 0
                index += 1
            elif s[index] == ')':
                # ')' marks end of expression within a set of parenthesis
                # First complete the calculation in the parenthesis 
                result += sign * cur_num

                # apply the sign before the parenthesis
                result *= stack.pop()
                
                # as stack.pop() is the result calculated before this parenthesis
                # stack.pop() + sign on stack * result from parenthesis
                result += stack.pop()

                cur_num = 0
                index += 1
        
        return result + sign * cur_num