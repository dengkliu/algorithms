// An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

// graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

// Return the length of the shortest path that visits every node. 

// You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

// 1 <= graph.length <= 12
// 0 <= graph[i].length <= graph.length

// Input: graph = [[1,2,3],[0],[0],[0]]
// Output: 4
// Explanation: 
// One possible path is [1,0,2,0,3]

// BFS的本质是什么？是从一个状态，通过某种规则，转移到下一个状态，知道到达终止状态。
// 我们的初始状态 - 所有点都没有被访问过。
// 我们的终止状态 - 从某个点出发，所有点都被访问过了

// 因为我们并不清楚从那个点出发，我们可以试所有点，把所有点放在同一层（同一个状态上）
// 同时我们记录从每个点出发，已经访问了哪些点，如果我们发现所有点都被访问了，那就表示我们抵达了最终状态。

// 这也是多源BFS的思想。
// 举个例子，有ABC三个起点，问D离任意起点的最短路径。
// 如果你分别bfs每一个起点，你只能分别得到D与A的最短距离、D与B的最短距离、D与C的最短距离，然后你还得再在三者之间取一个最小值。
// 如果你把ABC都放入队列进行BFS，那么当你第一次访问到D的时候就OK了，你不用关心这个最短距离到底是离A还是离B还是离C。

public class Solution {
    /**
     * @param graph: the graph
     * @return: the shortest path for all nodes
     */
    public int shortestPathLength(int[][] graph) {

        if (graph == null || graph.length == 0 || graph[0].length == 0) {
            return 0;
        }

        // Write your code here.
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[graph.length][1 << graph.length];

        // 我们可以reuse edge和revist node，因此不能直接用set排除已经被访问过得点
        // 我们需要排除的一种情况是，到达这个点，而且当前的状态已经存在了
        // 当前状态 --> 访问到了这些点
        // 也就是说 我们在之前某一步 已经出现过到达这个点 访问了这些点 
        // 那么我们现在没有必要继续下去 因为我们只会得到更多的步数 我们要找的是最短的步数
        // Set<Integer> visited = new HashSet<>();

        int end = 0;

        for (int i = 0; i < graph.length; i ++) {
            queue.offer(new int[]{i, 1 << i});
            visited[i][1 << i] = true;
            // End state 就是所有点都访问到了
            end = end | 1 << i;
        }

        // System.out.println("End: " + end);

        int step = 1;

        while (!queue.isEmpty()) {

            int size = queue.size();

            // System.out.println("step: " + step);

            // System.out.println("queue size: " + size);

            for (int length = 0; length < size; length ++) {

                int[] curr = queue.poll();

                int currNum = curr[0];
                int currState = curr[1];

                // System.out.println("curr node: " + currNum);
                // System.out.println("curr state: " + currState);

                for (int next : graph[currNum]) {

                    // System.out.println("next num: " + next);

                    int nextState = currState | 1 << next;

                    // 已经访问过了，这一定不是最短的
                    if (visited[next][nextState]) {
                        continue;
                    }

                    // System.out.println("next state: " + nextState);
                    if (nextState == end) {
                        return step;
                    } 

                    // Add to queue and visited set
                    queue.add(new int[]{next, nextState});
                    visited[next][nextState] = true;
                }
            }

            step ++;
        }

        return step;

    }
}





