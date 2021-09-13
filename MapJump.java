// Given a map of n×n, each cell has a height. Each time you can only move to an adjacent cell, and the height difference between the two cells is required to not exceed target. 
// You cannot get out of the map. 
// Find the the smallest target that satisfies from the upper left corner (0, 0) to the lower right corner (n-1, n-1).

// 1. BFS 
//    You can try starting the upper left corner and do BFS. Keep record of the min target for each cell.
//    If this is the first time to reach this cell or if you find a smaller target for this cell,
//    you can add the cell back to the queue and update the target for this cell (use hashmap to store cell to target pair)

public class Solution {

    int[] deltaX = {1, -1, 0, 0};
    int[] deltaY = {0, 0, -1, 1};

    /**
     * @param arr: the map
     * @return:  the smallest target that satisfies from the upper left corner (0, 0) to the lower right corner (n-1, n-1)
     */
    public int mapJump(int[][] arr) {
        // Write your code here.

        if (arr == null || arr.length == 0 || arr[0].length == 0) {
            return 0;
        }

        int rowCnt = arr.length;
        int colCnt = arr[0].length;

        Queue<Integer> queue = new ArrayDeque<>();
        Map<Integer, Integer> numToTarget = new HashMap<>();

        queue.add(0);
        numToTarget.put(0, 0);

        while (!queue.isEmpty()) {
            
            int curr = queue.poll();
            int currX = curr/colCnt, currY = curr%colCnt;
            int currTarget = numToTarget.get(curr);

            for (int direction = 0; direction < 4; direction ++) {
                
                int nextX = currX + deltaX[direction];
                int nextY = currY + deltaY[direction];
                int next = nextX * colCnt + nextY;

                if (outOfBound(nextX, nextY, rowCnt, colCnt)) {
                    continue;
                }

                // 先求出这样走，目前的target
                int newTarget = Math.max(currTarget, Math.abs(arr[currX][currY] - arr[nextX][nextY]));

                // 如果没有找到更小的target，就不继续了
                if (numToTarget.containsKey(next)) {
                    int existingTarget = numToTarget.get(next);
                    if (existingTarget <= newTarget) {
                        continue;
                    }
                }

                // 如果是第一次到这个点，或者找到了更小的target，就更新下
                numToTarget.put(next, newTarget);
                queue.add(next);
            }
        }

        return numToTarget.get(rowCnt * colCnt - 1);
    }

    boolean outOfBound(int row, int col, int nextX, int nextY) {

        if (row < 0 || row >= nextX) {
            return true;
        }

        if (col < 0 || col >= nextY) {
            return true;
        }

        return false;
    }
}