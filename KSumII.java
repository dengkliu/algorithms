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

// DP 解法
// dp[i][j][k] -- 在第i个数时，加了j个数，和为k的解法有多少种 
public class Solution {
    /**
     * @param A: an integer array
     * @param k: a postive integer <= length(A)
     * @param target: an integer
     * @return: A list of lists of integer
     */
    public List<List<Integer>> kSumII(int[] A, int k, int target) {

        Arrays.sort(A);


        int rowCnt = A.length + 1;
        int colCnt = k + 1;
        int depCnt = target + 1;

        int [][][] dp = new int[rowCnt][colCnt][depCnt];

        // 需要一个map存放dp数组中每个位置对应的解
        Map<Integer, List<List<Integer>>> map = new HashMap<>();

        // dp[n][k][sum]
        // 在第n个数时候 1. 一共加了k个数 2. 得到sum ---> 有多少种方案？

        // 加0个数得到0，永远有一个方案
        for (int i = 0; i < A.length + 1; i ++) {
            dp[i][0][0] = 1;
            // 三维数组一维化
            // depth * (rowCnt * colCnt) + row * colCnt + col;
            int currPos = i * colCnt;
            List<List<Integer>> list = new ArrayList<>();
            list.add(new ArrayList<Integer>());
            map.put(currPos, list);
        }

        for (int i = 1; i <= A.length; i ++) {
            // 目前为止考虑了i个数 最多也就能加i个数
            for (int j = 1; j <= k && j <= i; j++) {
                for (int sum = 1; sum <= target; sum ++) {

                    // 构建当前的解法
                    List<List<Integer>> currCombs = new ArrayList<>();  

                    // 能加入这个数的话，就加入
                    if (A[i-1] <= sum) {
                        // 方案总数
                        dp[i][j][sum] += dp[i - 1][j - 1][sum - A[i - 1]];

                        // 具体方案
                        int prevPos = (sum - A[i - 1]) * (rowCnt * colCnt) 
                            + (i - 1) * colCnt + j - 1;

                        // 之前这个地方的解法可能不存在！
                        if (map.get(prevPos) !=  null) {
                            // 根据之前的具体方案生成当前的具体方案    
                            for (List<Integer> preComb : map.get(prevPos)) {
                                List<Integer> currComb = new ArrayList<Integer>(preComb);
                                currComb.add(A[i - 1]);
                                currCombs.add(currComb);
                            }
                        }
                    }

                    // 不加入这个数的方案总数
                    dp[i][j][sum] += dp[i-1][j][sum];

                    int prevPos2 = sum * (rowCnt * colCnt) + (i - 1) * colCnt + j;
                    
                    if (map.get(prevPos2) != null) {
                        currCombs.addAll(map.get(prevPos2));
                    }

                    int currPos = sum * (rowCnt * colCnt) + i * colCnt + j;

                    map.put(currPos, currCombs);
                }
            }
        }

        return map.get(rowCnt*colCnt*depCnt - 1);

    }

    

}