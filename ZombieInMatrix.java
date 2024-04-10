// https://www.lintcode.com/problem/598/

// Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).
// Zombies can turn the nearest people (up/down/left/right) into zombies every day, but can not through wall. 
// How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

//Input:
//[[0,1,2,0,0],
// [1,0,0,2,1],
// [0,1,0,0,0]]
// Output:
// 2

// Multi-source BFS，
// 1 - Add all sources into the queue (the nodes with 0 in-degree)
// 2 - level order traversal, get size = queue.size() then for (int i = 1; i < size; i ++)
// 3 - initialize level cnt to 1， and increment it by 1 after each level traversal 
// 4 - keep tracking the cnt of targets visited until all targets are visited

class GridType {
    static int HUMAN = 0;
    static int ZOMBIE = 1;
    static int WALL = 2;
}

public class Solution {

    int[] deltaX = new int[]{-1, 0, 0, 1};
    int[] deltaY = new int[]{0, 1, -1, 0};
    /**
     * @param grid: a 2D integer grid
     * @return: an integer
     */
    public int zombie(int[][] grid) {

        if (grid == null || grid.length == 0) {
            return 0;
        }

        int rowCnt = grid.length;
        int colCnt = grid[0].length;

        int humanCnt = 0;
        int humanTurnedCnt = 0;

        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();

        for (int i = 0; i < rowCnt; i ++) {
            for (int j = 0; j < colCnt; j++) {
                if (grid[i][j] == GridType.HUMAN) {
                    humanCnt ++;
                }

                if (grid[i][j] == GridType.ZOMBIE) {
                    queue.add(i * colCnt + j);
                    visited.add(i * colCnt + j);
                }
            }
        }

        if (humanCnt == 0) {
            return 0;
        }

        int days = 1;

        while(!queue.isEmpty()) {            
            // level traversal 
            int size = queue.size();

            // i < size not queue.size()! because queue size is changing
            for (int i = 0; i < size; i ++) {
                int curr = queue.poll();
                int currX = curr/colCnt, currY = curr%colCnt;

                 for (int direction = 0; direction < 4; direction ++) {
                    int nextX = currX + deltaX[direction];
                    int nextY = currY + deltaY[direction];
                    int next = nextX * colCnt + nextY;

                    if (nextX < 0 || nextX >= rowCnt || nextY < 0 || nextY >= colCnt) {
                        continue;
                    }

                    if (grid[nextX][nextY] != GridType.HUMAN || visited.contains(next)) {
                        continue;
                    }

                    queue.add(next);
                    visited.add(next);
                    humanTurnedCnt++;
                    // no need to traverse more, all targets visited
                    if (humanTurnedCnt == humanCnt) {
                        return days;
                    }
                }
            }

            // increment the level cnt
            days ++;
        }

        return -1;
    }
}
