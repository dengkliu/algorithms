// There is a one-dimensional board with a starting point on the far left side of the board and an end point on the far right side of the board. 
// There are several positions on the board that are connected to other positions, ie if A is connected to B, 
// then when chess falls at position A, you can choose whether to give up to throw dice and move the chess from A to B directly. 
// And the connection is one way, which means that the chess cannot move from B to A. 
// Now given the length and connections of the board, and you have a six-sided dice(1-6), output the minimum steps to reach the end point.

// The index starts from 1.
// length > 1
// The starting point is not connected to any other location
// connections[i][0] < connections[i][1]

// 原本是个复杂图 因为有些点之间是1 有些点之间距离是0
// 希望转化为简单图
// 对于每个点 走一步能到的点在距离1到6之间 以及从这些可以直接连通的点 
// 要找一个点直接连通的点，也需要做BFS
// 因此解法1为 外层BFS找最短距离 内层BFS找直接连通的点

public class Solution {
    /**
     * @param length: the length of board
     * @param connections: the connections of the positions
     * @return: the minimum steps to reach the end
     */
    public int modernLudo(int length, int[][] connections) {

    	// 先 build graph, java 用hashmap
        Map<Integer, Set<Integer>> conntectedGraph = getGraph(connections, length);

        // Initialize DS for BFS
        Queue<Integer> queue = new ArrayDeque<>();
        // Since we need steps we use a map to record distance
        Map<Integer, Integer> distance = new HashMap<>();

        queue.add(1);
        distance.put(1, 0);

        while(!queue.isEmpty()) {

            int curr = queue.poll();

            // 如果找到终点 直接返回
            if (curr == length) {
                return distance.get(curr);
            }

            // 这是直接掷骰子能到的点
            int maxNext = Math.min(curr + 6, length);
            for (int i = curr + 1; i <= maxNext; i ++) {

                // Use BSF to find next positions for each of current positions
                List<Integer> nextPositions = 
                    findNextPositions(i, conntectedGraph, distance, length);

                for (int next: nextPositions) {
                    distance.put(next, distance.get(curr) + 1);
                    queue.offer(next);
                }
            }
        }

        return distance.get(length);

    }

    List<Integer> findNextPositions(int pos, 
        Map<Integer, Set<Integer>> conntectedGraph, 
        Map<Integer, Integer> distance,
        int length) {
        
        // 存放所有连通的点
        List<Integer> positions = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();

        queue.offer(pos);
        visited.add(pos);

        while(!queue.isEmpty()) {
            int curr = queue.poll();
            // 如果这个position已经存在于当前distance中
            // 说明已经找到过了 不可能找到更小的了的
            if (distance.containsKey(curr)) {
                continue;
            }
            positions.add(curr);
            for (Integer next : conntectedGraph.get(curr)) {
                if (distance.containsKey(next) || visited.contains(next)) {
                    continue;
                }
                queue.offer(next);
                visited.add(next);
            }
        }

        return positions;
    }

    Map<Integer, Set<Integer>> getGraph(int[][] connections, int length) {

        Map<Integer, Set<Integer>> graph = new HashMap<>();

        for (int i = 1; i <= length; i++) {
            graph.put(i, new HashSet<>());
        }

        for (int[] connection : connections) {
            graph.get(connection[0]).add(connection[1]);
        }

        return graph;
    }
}

// DP

// At each position, the min step = min(min step of all postions that direct connect this position, 
// min step of all positions that can reach this positin by one step + 1 )
public class Solution {
    /**
     * @param length: the length of board
     * @param connections: the connections of the positions
     * @return: the minimum steps to reach the end
     */
    public int modernLudo(int length, int[][] connections) {

        // dp[i] -- 从1到i最少需要多少步
        int[] dp = new int[length + 1];

        dp[0] = dp[1] = 0;

        for (int i = 2; i < length + 1; i ++) {

            int minSteps = Integer.MAX_VALUE;

            int minPre = Math.max(1, i - 6);

            for (int j = minPre; j < i; j ++) {
                minSteps = Math.min(minSteps, dp[j] + 1);
            }

            for (int[] connection : connections) {
                if (i == connection[1]) {
                    minSteps = Math.min(minSteps, dp[connection[0]]);
                }
            }
            
            dp[i] = minSteps;
        }

        return dp[length];
    }
}

