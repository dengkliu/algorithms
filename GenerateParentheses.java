// https://www.lintcode.com/problem/427/

// Given n, and there are n pairs of parentheses, write a function to generate all combinations of well-formed parentheses, 
// And return the combination result.

// Input: 3
// Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

// 典型的DFS问题
// 从上一个推下一个
// 对于每一个pre 可以生成 （pre） pre() 和 ()pre
// 但是要求pre本身是一个valid的parenthese
// 会漏掉比如 (())(()) 这种情况 因为 ())(() 不是一个valid parenthese

// 因此搜素树变成 一个个加左括号或者右括号
// 在每一个节点 规则是 左括号不能超过总括号数的一半 右括号数不能超过左括号数
// 还需要一个参数记录目前已经加了多少括号了
// 如果到了2*n 就得到了一个解 返回

// 假设 n = 2
//             ""
//             /\
//            (  )
//           / \  \ 
//          (( ()  *
//         / \  \
//        * (() ()(
//           |   |
//          (()) ()()

public class Solution {
    /**
     * @param n: n pairs
     * @return: All combinations of well-formed parentheses
     */

    // (())(()) --> ())(()
    // 无法根据 规则（ pre ） + () pre + pre () 得到
    public List<String> generateParenthesis(int n) {

        List<String> result = new ArrayList<>();

        if (n == 0) {
            return result;
        }

        int leftNum = 0;
        int rightNum = 0;

        dfs(n, 0, result, leftNum, rightNum, "");

        return result;
    }

    void dfs(int n, int k, List<String> result, int leftNum, int rightNum, String curr) {

        if (rightNum > leftNum) {
            return;
        }

        if (leftNum > n) {
            return;
        }

        if (k == n * 2) {
            result.add(curr);
            return;
        }

        dfs(n, k + 1, result, leftNum + 1, rightNum, curr + "(");
        dfs(n, k + 1, result, leftNum, rightNum + 1, curr + ")");
    }

}