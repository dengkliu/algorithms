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

// 多源BFS，有点像元胞自动机
// 要点1 - 第一次要把所有源头加进去
// 要点2 - 分层遍历，每一次记录size = queue.size() 然后 for (int i = 1; i < size; i ++)
// 要点3 - 层数初始化为1， 在每次分层处理的for loop完成后，层数加一
// 要点4 - 记录被扫到的目标数，每次扫到一个就判断有没有扫到全部，提前退出，返回层数。因为这样可避免进入无效的下一层，即已经没有任何目标可以扫描

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
            // 分层遍历
            int size = queue.size();

            // i < size 而不是小于queue.size()! 
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
                    // 一定得提前check 当全部扫到的时候，没有必要进入下一层了
                    if (humanTurnedCnt == humanCnt) {
                        return days;
                    }
                }
            }

            // 增加天数
            days ++;
        }

        return -1;
    }
}
