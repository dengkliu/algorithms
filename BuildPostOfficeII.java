// https://www.lintcode.com/problem/573

// Given a 2D grid, each cell is either a wall 2, 
// an house 1 or empty 0 (the number zero, one, two), 
// find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

// Returns the sum of the minimum distances from all houses to the post office. Return -1 if it is not possible.

// You cannot pass through wall and house, but can pass through empty.
// You only build post office on an empty.

// Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
// Output：8
// Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.

// Shortest distance on 2D array - BFS

// 1. Enumerate the empty places and for each do bfs to get shortest distance to each house. 
// 2. Enumerate the houses and get distances to this house for all empty places.

// #2 is better than #1 if there are many empty places and a few house.


// 常量 定义在solution class 外面 增加代码可读性
class GridType {
    static int EMPTY = 0;
    static int HOUSE  = 1;
    static int WALL = 2;
}

public class Solution {
    
    // 偏移量 矩阵中游走的小套路
    int[] deltaX = {0, 1, -1, 0};
    int[] deltaY = {1, 0, 0, -1};

    
    /**
     * @param grid: a 2D grid
     * @return: An integer
     */
    public int shortestDistance(int[][] grid) {

        if (grid == null || grid.length == 1) {
            return 0;
        }

        // 最后我们需要知道 1. 这个格子能不能到所有houses 2.这个格子到所有Houses的最短距离是多少
        int[][] distanceSum = new int[grid.length][grid[0].length];
        int[][] reachableHouseCnt = new int[grid.length][grid[0].length];

        // 记录一共有多少Houses
        int houseCnt = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
            	// 如果是house 开始bfs 更新两个数组
                if(grid[i][j] == GridType.HOUSE) {
                    houseCnt ++;
                    bfs(i, j, grid, distanceSum, reachableHouseCnt);
                }
            }
        }

        int minDistances = Integer.MAX_VALUE;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == GridType.EMPTY && reachableHouseCnt[i][j] == houseCnt) {
                    minDistances = Math.min(minDistances, distanceSum[i][j]);
                }
            }
        }

        return minDistances == Integer.MAX_VALUE ? -1 : minDistances;

    }

    void bfs(int x, int y, int[][] grid, int[][] distanceSum, int[][] reachableHouseCnt) {

        int colCnt = grid[0].length;

        Queue<Integer> queue = new ArrayDeque<>();
        Map<Integer, Integer> distance = new HashMap<>();

        int start = x * colCnt + y;

        queue.add(start);
        distance.put(start, 0);

        while(!queue.isEmpty()) {

            int curr = queue.poll();
            int currX = curr/colCnt;
            int currY = curr%colCnt;

            for (int i = 0; i < 4; i ++) {

                int nextX = currX + deltaX[i];
                int nextY = currY + deltaY[i];

                if (!isValid(nextX, nextY, grid, distance)) {
                    continue;
                }

                // 找到了到这块空地的最短距离
                distance.put(nextX * colCnt + nextY, distance.get(curr) + 1);

                // 更新当前最短距离的总和
                distanceSum[nextX][nextY] += distance.get(curr) + 1;
                reachableHouseCnt[nextX][nextY] ++;

                queue.add(nextX * colCnt + nextY);
            }
        }
    }

    // 在矩阵范围中 不在visied之中 并且是空地
    boolean isValid(int x, int y, int[][] grid, Map<Integer, Integer> distance) {

        if (x < 0 || x >= grid.length) {
            return false;
        }

        if (y < 0 || y >= grid[0].length) {
            return false;
        }

        if (distance.containsKey(x * grid[0].length + y)) {
            return false;
        }

        return grid[x][y] == GridType.EMPTY;

    }

}
