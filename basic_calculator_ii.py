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
        previous_operator = "+"

        #  3 + 2 * 2
        # [3, 4]
        while index < len(s):
            c = s[index]
            if c == " ":
                index += 1
            elif c.isdigit():
                num = int(c)
                index += 1
                while index < len(s) and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                if previous_operator == "+":
                    stack.append(num)
                elif previous_operator == "-":
                    stack.append(-num)
                elif previous_operator == "*":
                    prev_num = stack.pop()
                    stack.append(prev_num * num)
                elif previous_operator == "/":
                    prev_num = stack.pop()
                    division_num = prev_num // num
                    if division_num < 0 and prev_num % num != 0:
                        stack.append(division_num + 1)
                    else:
                        stack.append(division_num)
            else:
                previous_operator = c
                index += 1

        return sum(stack)



# O(1) 空间优化版
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        result = 0
        last_num = 0
        curr_operation = '+'
        index = 0

        # 3 + 2 * 2 
        # 
        # last = 0  result = 0 
        # last = 3  result = 0
        # last = 2  result = 3
        # last = 4  result = 3 
        # 7
        while index < len(s):
            letter = s[index]
            if letter.isdigit():
                cur_num = int(letter)
                index = index + 1
                while index < len(s) and s[index].isdigit():
                    cur_num = cur_num * 10 + int(s[index])
                    index = index + 1
                if curr_operation == '+' or curr_operation == '-':
                    result += last_num
                    last_num = cur_num if curr_operation == '+' else - cur_num
                elif curr_operation == '*':
                    last_num = last_num * cur_num
                elif curr_operation == '/':
                    division_num = last_num // cur_num
                    if division_num < 0 and last_num % cur_num != 0:
                        last_num = division_num + 1
                    else:
                        last_num = division_num
            elif letter.isspace():
                index += 1
            else:
                curr_operation = letter
                cur_num = 0
                index += 1
                

        return result + last_num
