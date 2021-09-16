// https://www.lintcode.com/problem/90

// Given n unique postive integers, number k (1 <= K <= N) and target.
// Find all possible k integers where their sum is target.

// array = [1,2,3,4]
// k = 2
// target = 5

// 典型的DFS 组合类问题

// 搜索树
//        /           \        \        \ 
//       1             2        3       4
//      /|\           /|       /        |  
//     2 3 4         3 4       4        no more options
//    /  |  \       /  |       |
//   no  no  yes   yes no      no

// 每个节点需要哪些参数
// 1. 当前要加的是那个数（index）
// 2. 当前加了几个数
// 3. 一共可以加几个数
// 4. 当前的sum是多少
// 5. 一共的target是多少
// 6.还需要一个变量来存储结果
// 2 & 3 可以合并为 当前还可以加几个数 跟0作比较 如果不能再加数了 就返回
// 4 & 5 可以合并为 当前还有多少sum需要加 跟0作比较 如果为0 而且当前不可再加数 那就得到了一个满足条件的方案

public class Solution {
    /**
     * @param A: an integer array
     * @param k: a postive integer <= length(A)
     * @param target: an integer
     * @return: A list of lists of integer
     */
    public List<List<Integer>> kSumII(int[] A, int k, int target) {

        Arrays.sort(A);

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();

        dfs(0, k, target, A, result, list);

        return result;

    }

    void dfs(int index, int numOfNumLeft, int sumLeft, int[] A, List<List<Integer>> result, List<Integer> list) {

        if (numOfNumLeft == 0 && sumLeft == 0) {
            // 一定要copy，list参数会在内存里被反复修改
            result.add(new ArrayList<Integer>(list));
            return;
        }

        if (numOfNumLeft == 0 || sumLeft == 0) {
            return;
        }

        for (int i = index; i < A.length; i ++) {
            // 把要加的数字放进去
            list.add(A[i]);
            // 修改参数
            // 1. 下一个要加的数在i + 1
            // 2. 剩下可以加的数字数量减1
            // 3. 剩下可以加的数字和减去当前加进去的数字
            // 4. 更新后的list
            dfs(i + 1, numOfNumLeft - 1, sumLeft - A[i], A, result, list);
            // 还原加进去的数字
            // ArrayList remove(int index)
            list.remove(list.size() - 1);
        }
    }
}