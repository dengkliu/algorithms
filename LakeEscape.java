// https://www.lintcode.com/problem/1828/

// Albert is stranded on a frozen lake. He is currently on a snowbank that gives him some traction. 
// but once he steps the ice, he will slide in the same direction until he hits another snowbank. 
// There are also treacherous holes in the ice that he must avoid.

// As a cruel twist of fate, Albert's young pup, Kuna, is also stranded, but on a different snowbank. 
// Can Albert reach his pup AND make it to shore?

// Albert can only move horizontally and vertically. He makes it to shore by leaving the lake grid.

// The input contains these parameters:

// side_length: the length of a side of the lake (it's a square)
// lake_grid: a 2D matrix representing the lake 0 = ice, 1 = snowbank, -1 = hole
// albert_row: row of Alber'ts snowbank
// albert_column: column of Albert's snowbank
// kuna_row: row of Kuna's snowbank
// kuna_column: column of Kuna's snowbank

// 充要条件 - 从起始点 1.要能找到狗 2.要能上岸

// 连通性问题，一遍BFS就可以


class GridType {
    static int ICE = 0;
    static int SNOWBANK = 1;
    static int HOLE = -1;
}

public class Solution {

    int[] deltaX = {-1, 1, 0, 0};
    int[] deltaY = {0, 0, -1, 1};

    /**
     * @param side_length: the length of a side of the lake (it's a square)
     * @param lake_grid: a 2D matrix representing the lake 0= ice, 1= snowbank, -1= hole 
     * @param albert_row: row of Albert's snowbank
     * @param albert_column: column of Albert's snowbank 
     * @param kuna_row: row of Kuna's snowbank 
     * @param kuna_column: column of Kuna's snowbank
     * @return: a bool - whether Albert can escape
     */
    public boolean lakeEscape(int side_length, int[][] lake_grid, int albert_row, int albert_column, int kuna_row, int kuna_column) {

        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();

        boolean canExit = false;
        boolean canReachKuna = false;

        queue.add(albert_row * side_length + albert_column);
        visited.add(albert_row * side_length + albert_column);

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            int currX = curr/side_length;
            int currY = curr%side_length;

            for (int direction = 0; direction < 4; direction ++) {

                int nextX = currX + deltaX[direction];
                int nextY = currY + deltaY[direction];

                // 只要在界内，而且是冰，就一直滑
                while (!outOfBound(nextX, nextY, side_length) && lake_grid[nextX][nextY] == GridType.ICE) {
                    nextX += deltaX[direction];
                    nextY += deltaY[direction];
                }

                // 在界外，说明能上岸，先不考虑这个方向了
                if (outOfBound(nextX, nextY, side_length)) {
                    canExit = true;
                    continue;
                }

                // 不能走这个方向
                if (lake_grid[nextX][nextY] == GridType.HOLE) {
                    continue;
                }

                // 否则便是碰到snowbank，注意可以停在snowbank 
                // 所以只要这个是个新的位置 就可以加进queue里去

                if (visited.contains(nextX * side_length + nextY)) {
                    continue;
                }
                queue.add(nextX * side_length + nextY);
                visited.add(nextX * side_length + nextY);

                // 看看是否找到了狗
                if (nextX == kuna_row && nextY == kuna_column) {
                    canReachKuna = true;
                }

            }

            if (canReachKuna && canExit) {
                return true;
            }
        }

        return false;
    }

    boolean outOfBound(int row, int col, int side_length) {

        if (row < 0 || row >= side_length) {
            return true;
        }

        if (col < 0 || col >= side_length) {
            return true;
        }

        return false;
    }
}
