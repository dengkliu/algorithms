# https://leetcode.com/problems/remove-invalid-parentheses/description/

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.valid_expressions = set()
        self.min_removed = float('inf')

        def dfs(index, left_cnt, right_cnt, cur_str, removed_cnt):
            if index == len(s):
                if left_cnt == right_cnt:
                    if removed_cnt == self.min_removed:
                        self.valid_expressions.add(''.join(cur_str))
                    elif removed_cnt < self.min_removed:
                        self.min_removed = removed_cnt
                        self.valid_expressions = set()
                        self.valid_expressions.add(''.join(cur_str))
                return

            if s[index] != '(' and s[index] != ')':
                cur_str.append(s[index])
                dfs(index + 1, left_cnt, right_cnt, cur_str,  removed_cnt)
            else:
                dfs(index + 1, left_cnt, right_cnt, cur_str, removed_cnt + 1)
                if s[index] == '(':
                    cur_str.append('(')
                    dfs(index + 1, left_cnt + 1, right_cnt, cur_str, removed_cnt)
                elif right_cnt < left_cnt:
                    cur_str.append(')')
                    dfs(index + 1,  left_cnt, right_cnt + 1, cur_str, removed_cnt)
                    
                
        dfs(0, 0, 0, [], 0)

        return list(self.valid_expressions)