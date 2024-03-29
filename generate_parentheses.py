# https://leetcode.com/problems/generate-parentheses/

# Given n, and there are n pairs of parentheses, write a function to generate all combinations of well-formed parentheses, 
# And return the combination result.

# Input: 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# 典型的DFS问题
# 从上一个推下一个
# 对于每一个pre 可以生成 （pre） pre() 和 ()pre
# 但是要求pre本身是一个valid的parenthese
# 会漏掉比如 (())(()) 这种情况 因为 ())(() 不是一个valid parenthese

# 因此搜素树变成 一个个加左括号或者右括号
# 在每一个节点 规则是 左括号不能超过总括号数的一半 右括号数不能超过左括号数
# 还需要一个参数记录目前已经加了多少括号了
# 如果到了2*n 就得到了一个解 返回

# 假设 n = 2
#             ""
#             /\
#            (  )
#           / \  \ 
#          (( ()  *
#         / \  \
#        * (() ()(
#           |   |
#          (()) ()()

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        if n <= 0:
            return result

        self._dfs("", 0, 0, 0, n, result)

        return result

    
    def _dfs(self, curr, open_cnt, close_cnt, total_cnt, n, result):
        # this is where you want to stop the dfs because you know it violates the requirements
        if close_cnt > open_cnt:
            return
            
        # this is where you want to stop the dfs because you know it violates the requirements
        if open_cnt > n:
            return

        # this is where you wanna stop the dfs and return because you know you reach the destination
        if total_cnt == 2 * n:
            result.append(curr)
            return
        
        self._dfs(curr + "(", open_cnt + 1, close_cnt, total_cnt + 1, n, result)
        self._dfs(curr + ")", open_cnt, close_cnt + 1, total_cnt + 1, n, result)


# backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()
        backtracking([], 0, 0)
        return answer
