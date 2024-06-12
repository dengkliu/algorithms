# https://leetcode.com/problems/basic-calculator-iii/

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def resolve_operation(operation, cur_num, pre_num):
            if operation == '+':
                return cur_num
            elif operation == '-':
                return -cur_num
            elif operation == '*':
                return pre_num * cur_num
            else:
                if pre_num // cur_num < 0 and pre_num % cur_num != 0:
                    return pre_num // cur_num + 1
                else:
                    return pre_num // cur_num

        stack = []
        cur_operation = '+'
        index = 0

        # 3 + (2 * 2 + 2)
        while index < len(s):
            letter = s[index]
            if letter.isspace():
                index += 1
            elif letter.isdigit():
                num = int(letter)
                index += 1
                while index < len(s) and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                if cur_operation == '+' or cur_operation == '-':
                    stack.append(resolve_operation(cur_operation, num, 0))
                else:
                    pre_num = stack.pop()
                    stack.append(resolve_operation(cur_operation, num, pre_num))                
            elif letter == '(':
                stack.append(cur_operation)
                # reset the cur_operation
                cur_operation = '+'
                index += 1
            elif letter == ')':
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                operation = stack.pop()
                if operation == '+' or operation == '-':
                    stack.append(resolve_operation(operation, num, 0))
                else:
                    pre_num = stack.pop()
                    stack.append(resolve_operation(operation, num, pre_num))    
                cur_operation = '+'
                index += 1
            else:
                cur_operation = letter
                index += 1
        
        return sum(stack)