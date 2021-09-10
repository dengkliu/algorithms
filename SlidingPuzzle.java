// On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
// A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
// The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

// Given a puzzle board, return the least number of moves required so that the state of the board is solved. 
// If it is impossible for the state of the board to be solved, return -1.

// board will be a 2 x 3 array as described above.
// board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

// Given board = `[[1,2,3],[4,0,5]]`, return `1`.

// Explanation: 
// Swap the 0 and the 5 in one move.

// 典型的BSF题 给定起始状态和转换规则 求到最终状态的最少转换次数

public class Solution {

	// 二维矩阵移动小技巧
    int[] deltaX = {0, 1, -1, 0};
    int[] deltaY = {1, 0, 0, -1};

    /**
     * @param board: the given board
     * @return:  the least number of moves required so that the state of the board is solved
     */
    public int slidingPuzzle(int[][] board) {

        Queue<String> queue = new ArrayDeque<>();
        Map<String, Integer> distance = new HashMap<>();

        int[][] end = new int[][]{{1, 2, 3}, {4, 5, 0}};

        // 想想怎么记录一个矩阵状态 好用来比较？
        // 把矩阵转化为一个string
        String start = boardToStr(board);  
        String target = boardToStr(end);

        queue.offer(start);
        distance.put(start, 0);

        while(!queue.isEmpty()) {

            String curr = queue.poll();

            if (curr.equals(target)) {
                return distance.get(target);
            }

            for (int direction = 0; direction < 4; direction ++) {
                String next = getNextBoardStr(curr, direction, board);

                if (next == null || distance.containsKey(next)) {
                    continue;
                }

                distance.put(next, distance.get(curr) + 1);
                queue.offer(next);
            } 
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

    String getNextBoardStr(String curr, int direction, int[][] board) {
        int zeroIndex = curr.indexOf('0');
        int zeroRow = zeroIndex/board[0].length, zeroCol = zeroIndex%board[0].length;

        int nextZeroRow = zeroRow + deltaX[direction], nextZeroCol = zeroCol + deltaY[direction]; 

        if (nextZeroRow < 0 || nextZeroRow >= board.length 
            || nextZeroCol < 0 || nextZeroCol >= board[0].length) {
            return null;
        }

        // Do a swap! String.toCharArray()
        char[] chars = curr.toCharArray();
        char temp = chars[nextZeroRow * board[0].length + nextZeroCol];
        chars[nextZeroRow * board[0].length + nextZeroCol] = '0';
        chars[zeroRow * board[0].length + zeroCol] = temp;

        // You can initialize a string from a char array!
        return new String(chars);

    }
}