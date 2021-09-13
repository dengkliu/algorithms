// https://www.lintcode.com/problem/261/

// There is a two-dimensional array, only consists of 0 and 1.
// You can change a 0 to 1 at most once, please calculate the maximum area of connected 1s.
// If two 1s are adjcent up to down or left to right, they are regrarded connected.

// The two-dimensional array has nn rows and mm columns, 1 <= n, m <=500.
// In example, change any 00 to 11, you can get a connection with an area 33.

// Input：
// [[0,1]
// ,[1,0]]
// Output：
// 3

// 连通性问题 很明显的BSF或者Union Find
// 这道题 需要记录每个连通块的size 可以用BSF 但是也需要对连通块进行编号 用hashmap存放面积
// 也可以直接用Union Find, 每个连通块用root识别 然后记录每个连通块的大小

// 然后再次遍历整个数组 对于每个0 找到附近的所有连通块 然后把面积加起来

class UnionFind {

    Map<Integer, Integer> father;

    Map<Integer, Integer> sizeOfSet;

    public UnionFind() {
        father = new HashMap<>();
        sizeOfSet = new HashMap<>();
    }

    void add(int num) {
        if (father.containsKey(num)) {
            return;
        }

        // 初始化father为null
        father.put(num, null);
        sizeOfSet.put(num, 1);

        Set<Integer> set = new HashSet<>();
        set.add(num);
    }

    int find(int num) {
        int root = num;

        while(father.get(root) != null) {
            root = father.get(root);
        }

        // 路径压缩
        while(num != root) {
            int originalParent = father.get(num);
            father.put(num, root);
            num = originalParent;
        }
        
        return root;
    }

    boolean isConnected(int num1, int num2) {
        return find(num1) == find(num2);
    }

    void merge(int num1, int num2) {
        int root1 = find(num1);
        int root2 = find(num2);

        if (root1 != root2) {
            father.put(root1, root2);
            sizeOfSet.put(root2, sizeOfSet.get(root1) + sizeOfSet.get(root2));
        }
    }
}


public class Solution {

    private int[] deltaX = {-1, 1, 0, 0};
    private int[] deltaY = {0, 0, -1, 1};

    /**
     * @param matrix: the matrix for calculation.
     * @return: return the max area after operation at most once.
     */
    public int maxArea(int[][] matrix) {

        if (matrix == null || matrix.length == 0) {
            return 0;
        }

        int rowCnt = matrix.length;
        int colCnt = matrix[0].length;

        UnionFind uf = new UnionFind();

        int maxArea = 0;

        // 先建立所有连通块，存储每个联通块的大小
        for (int i = 0; i < matrix.length; i ++) {
            for (int j = 0; j < matrix[0].length; j ++) {

                if (matrix[i][j] == 1) {

                    // 如果这是块陆地，就加到uf中去
                    // 并且和四个方向上的陆地合并
                    uf.add(i * colCnt + j);

                    for (int direction = 0; direction < 4; direction ++) {

                        int neighborX = i + deltaX[direction];
                        int neighborY = j + deltaY[direction];

                        if (neighborX < 0 || neighborX >= rowCnt || neighborY < 0 || neighborY >= colCnt) {
                            continue;
                        }

                        if (matrix[neighborX][neighborY] == 0) {
                            continue;
                        }

                        if (!uf.father.containsKey(neighborX * colCnt + neighborY)) {
                            continue;
                        }

                        uf.merge(i * colCnt + j, neighborX * colCnt + neighborY);
                    }

                    maxArea = Math.max(maxArea, uf.sizeOfSet.get(uf.find(i * colCnt + j)));
                }
            }
        }

        for (int i = 0; i < matrix.length; i ++) {
            for (int j = 0; j < matrix[0].length; j ++) {

                if (matrix[i][j] == 0) {

                    List<Integer> roots = new ArrayList<>();

                    int currArea = 0;

                    for (int direction = 0; direction < 4; direction ++) {
                        int neighborX = i + deltaX[direction];
                        int neighborY = j + deltaY[direction];

                        if (neighborX < 0 || neighborX >= rowCnt || neighborY < 0 || neighborY >= colCnt) {
                            continue;
                        }

                        if (matrix[neighborX][neighborY] == 0) {
                            continue;
                        }

                        // 假如是块陆地，而且是个新的连通块，把root加进来
                        if (roots.contains(uf.find(neighborX * colCnt + neighborY))) {
                            continue;
                        }

                        roots.add(uf.find(neighborX * colCnt + neighborY));
                    }

                    // 累加所有之前不相通的连通块面积
                    for (int root : roots) {
                        currArea += uf.sizeOfSet.get(root);
                    }

                    // 打擂台，更新最大面积
                    maxArea = Math.max(maxArea, currArea + 1);
                }
            }
        }

        return maxArea;
    }
}
