// https://www.lintcode.com/problem/677

// Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. 
// If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

// Find the number of islands that size bigger or equal than K.

// Input: 
// [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
// 2
// Output: 2
// Explanation:
// the 2D grid is
// [
//  [1, 1, 0, 0, 0],
//  [0, 1, 0, 0, 1],
//  [0, 0, 0, 1, 1],
//  [0, 0, 0, 0, 0],
//  [0, 0, 0, 0, 1]
// ]
// there are two island which size is equals to 3.

public class Solution {

    int[] deltaX = {0, 1, -1, 0};
    int[] deltaY = {1, 0, 0, -1};

    /**
     * @param grid: a 2d boolean array
     * @param k: an integer
     * @return: the number of Islands
     */
    public int numsofIsland(boolean[][] grid, int k) {

        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int rowCnt = grid.length;
        int colCnt = grid[0].length;

        int[] result = new int[1];

        // 避免更改原始数据，整体上用一个set存放所有已经访问过的位置
        Set<Integer> visited = new HashSet<>();

        for (int i = 0; i < rowCnt; i ++) {
            for (int j = 0; j < colCnt; j ++) {
                if (grid[i][j] && !visited.contains(i*colCnt + j)) {
                    bsf(i, j, visited, result, rowCnt, colCnt, grid, k);
                }
            }
        }

        return result[0];
    }

    void bsf(int row, int col, 
        Set<Integer> visited, int[] result, 
        int rowCnt, int colCnt, boolean[][] grid, int k) {

        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> island = new HashSet<>();

        queue.offer(row * colCnt + col);
        island.add(row * colCnt + col);
        visited.add(row * colCnt + col);

        while(!queue.isEmpty()) {
            
            int curr = queue.poll();

            for (int direction = 0; direction < 4; direction ++) {
                
                int next = getNextIsland(curr, direction, rowCnt, colCnt, grid);

                if (next != -1 && !visited.contains(next) && !island.contains(next)) {
                    queue.offer(next);
                    island.add(next);
                    visited.add(next);
                }
            }
        }
        
        if (island.size() >= k) {
            result[0]++;
        }
    }

    int getNextIsland(int curr, int direction, int rowCnt, int colCnt, boolean[][] grid) {

        int currX = curr/colCnt, currY = curr%colCnt;
        int nextX = currX + deltaX[direction], nextY = currY + deltaY[direction];

        if (nextX < 0 || nextX >= rowCnt || nextY < 0 || nextY >= colCnt) {
            return -1;
        }

        if (!grid[nextX][nextY]) {
            return -1;
        }

        return nextX * colCnt + nextY;

    }
}

