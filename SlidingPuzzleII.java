// On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.
// A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
// Given an initial state of the puzzle board and final state, 
// return the least number of moves required so that the initial state to final state.
// If it is impossible to move from initial state to final state, return -1.

// Input:
//[
// [2,8,3],
// [1,0,4],
// [7,6,5]
//]
//[
// [1,2,3],
// [8,0,4],
// [7,6,5]
//]

// Output: 4

// 在明确知道起始和终点的情况下，可以开始双向BFS
public class Solution {

    // 二维矩阵移动小技巧
    int[] deltaX = {0, 1, -1, 0};
    int[] deltaY = {1, 0, 0, -1};

    /**
     * @param init_state: the initial state of chessboard
     * @param final_state: the final state of chessboard
     * @return: return an integer, denote the number of minimum moving
     */
    public int minMoveStep(int[][] init_state, int[][] final_state) {

        int rowCnt = init_state.length;
        int colCnt = init_state[0].length;

        // 想想怎么记录一个矩阵状态 好用来比较？
        // 把矩阵转化为一个string
        String start = boardToStr(init_state);  
        String target = boardToStr(final_state);
        
        Queue<String> forwardQueue = new ArrayDeque<>();
        Map<String, Integer> forwardDistance = new HashMap<>();

        Queue<String> backwardQueue = new ArrayDeque<>();
        Map<String, Integer> backwardDistance = new HashMap<>();

        forwardQueue.add(start);
        forwardDistance.put(start, 0);
        backwardQueue.add(target);
        backwardDistance.put(target, 0);

        while(!forwardQueue.isEmpty() && !backwardQueue.isEmpty()) {

            int result;

            result = extend(forwardQueue, forwardDistance, backwardDistance, rowCnt, colCnt);

            if (result != -1) {
                return result;
            }
            
            result = extend(backwardQueue, backwardDistance, forwardDistance, rowCnt, colCnt);

            if (result != -1) {
                return result;
            }
        }

        return forwardDistance.getOrDefault(target, -1);
    }

    int extend(Queue<String> queue, 
        Map<String, Integer> map, Map<String, Integer> targetMap, int rowCnt, int colCnt) {

        String curr = queue.poll();

        for (int direction = 0; direction < 4; direction ++) {
            
            String next = getNextBoardStr(curr, direction, rowCnt, colCnt);

            if (next == null || map.containsKey(next)) {
                continue;
            }

            // 相遇了
            if (targetMap.containsKey(next)) {
                return map.get(curr) + 1 + targetMap.get(next);
            }

            map.put(next, map.get(curr) + 1);
            queue.offer(next);
        } 

        return -1;
    }

    String boardToStr(int[][] board) {
        
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < board.length; i ++) {
            for (int j = 0; j < board[0].length; j ++) {
                sb.append(board[i][j] + "");
            }
        }

        return sb.toString();
    }

    String getNextBoardStr(String curr, int direction, int rowCnt, int colCnt) {
        
        int zeroIndex = curr.indexOf('0');
        int zeroRow = zeroIndex/colCnt, zeroCol = zeroIndex%colCnt;

        int nextZeroRow = zeroRow + deltaX[direction], nextZeroCol = zeroCol + deltaY[direction]; 

        if (nextZeroRow < 0 || nextZeroRow >= rowCnt 
            || nextZeroCol < 0 || nextZeroCol >= colCnt) {
            return null;
        }

        // Do a swap! String.toCharArray()
        char[] chars = curr.toCharArray();
        char temp = chars[nextZeroRow * colCnt + nextZeroCol];
        chars[nextZeroRow * colCnt + nextZeroCol] = '0';
        chars[zeroRow * colCnt + zeroCol] = temp;

        // You can initialize a string from a char array!
        return new String(chars);

    }
}