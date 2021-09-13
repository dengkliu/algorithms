// There is a ball in a maze with empty spaces and walls. 
// The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. 
// When the ball stops, it could choose the next direction. 
// There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

// Given the position of the ball, the position of the hole and the maze, 
// find out how the ball falls into the hole by moving the shortest distance. 
// The distance is defined by the number of empty spaces the ball passes from the starting position (excluded) to the hole (included). 
// Use "u", "d", "l" and "r" to output the direction of movement. 
// Since there may be several different shortest paths, you should output the shortest method in alphabetical order.
// If the ball doesn't go into the hole, output "impossible".

// The maze is represented by a binary 2D array. 
// 1 means the wall and 0 means the empty space. 
// You may assume that the borders of the maze are all walls. 
// The ball and the hole coordinates are represented by row and column indexes.

// Input:
// [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
// [4,3]
// [0,1]

// Output: "lul"

// BSF. 这是个复杂图，因为球会滚动，所以球到下一个停靠点的距离是不一样的。可以用SPFA.
// 那么我们就得知道，到达每个点的距离是多少，如果距离更小，我们就要将点重新入队。
// 注意题目要求字典序，所以即使距离一样，假如字典序更小，我们也得重新入队。
// 比较两个string的alphabetical order 要用String.compareTo
// 所以我们需要存放 1.距离 2.path 我们得用一个Pair class来存放这两个变量。

// 技巧1 - 把常量定义在solution class外面
class GridType {
    static int WALL = 1;
    static int EMPTY = 0;
}

// 到达每个点，我们需要知道 1. 距离 2. path，所以我们需要一个pair class来存放这些信息
// 把这个记录到distance map中去
class Pair {
    int dist;
    String path;
    
    Pair(int dist, String path){
        this.dist = dist;
        this.path = path;
    }
}

public class Solution {

	// 按照字母排序，同时也设定对应的delta数组
    String[] DIRECTION = new String[]{"d", "l", "r", "u"};
    int[] deltaX = new int[]{1, 0, 0, -1};
    int[] deltaY = new int[]{0, -1, 1, 0};

    /**
     * @param maze: the maze
     * @param ball: the ball position
     * @param hole: the hole position
     * @return: the lexicographically smallest way
     */
    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {

    	// Edge case处理
        if (maze == null || maze.length == 0 || maze[0].length == 0
            || ball.length == 0 || hole.length == 0) {
            return "impossible";
        }

        // 初始化DS
        Queue<Integer> queue = new ArrayDeque<>();
        Map<Integer, Pair> distance = new HashMap<>();

        int x = ball[0], y = ball[1];
        int colCnt = maze[0].length;

        // 小技巧2 - 存放二维数组坐标
        queue.add(x*colCnt + y);
        distance.put(x*colCnt + y, new Pair(0, ""));

        while(!queue.isEmpty()) {

            int curr = queue.poll();

            int currX = curr/colCnt, currY = curr%colCnt;

            // kick the ball for these 4 directions and get the next
            for (int direction = 0; direction < 4; direction ++) {

                int next = kickBall(currX, currY, direction, maze, hole);

                int nextX = next/colCnt, nextY = next%colCnt;

                // 看看到下个点距离是多少，求距离一定要加绝对值！
                int dist = distance.get(curr).dist + 
                    Math.abs(nextX - currX) + Math.abs(nextY - currY);
                // 先把path算出来
                String path = distance.get(curr).path + DIRECTION[direction];

                // 假如没找到更小的path，直接跳过
                if (distance.containsKey(next) && !shorterPathFound(next, distance, dist, path)) {
                    continue;
                }

                // 1. 第一次找到这个点 2. 找到了更小的path 都要入队并更新distance
                distance.put(next, new Pair(dist, path)); 
                queue.offer(next);
            }
        }

        // 不一定能找到，找得到的话才返回
        if (distance.containsKey(hole[0]*colCnt + hole[1])) {
            return distance.get(hole[0]*colCnt + hole[1]).path;
        }

        return "impossible";

    }
    
    int kickBall(int x, int y, int i, int[][] maze, int[] hole) {

        int dx = deltaX[i], dy = deltaY[i];

        while ((x != hole[0] || y != hole[1]) && !isWall(x, y, maze)) {
            x = x + dx;
            y = y + dy;
        }

        if (x == hole[0] && y == hole[1]) {
            return x * maze[0].length + y;
        }

        // 当前点是wall 不能停在wall这个点 所以返回上一个点
        return (x - dx) * maze[0].length + y - dy;

    }

    boolean isWall(int x, int y, int[][] maze) {

        // If it is out of the range, then it is a wall
        if (x < 0 || x >= maze.length 
            || y < 0 || y >= maze[0].length) {
                return true;
        }

        return maze[x][y] == GridType.WALL;
    }

    boolean shorterPathFound(int pos, Map<Integer, Pair> distance, int dist, String path) {
        
        int currDist = distance.get(pos).dist;
        String currPath = distance.get(pos).path;

        if (dist < currDist) {
            return true;
        }

        if (dist == currDist) {
            return path.compareTo(currPath) <= 0;
        }

        return false;
    }
}





