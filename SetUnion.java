// https://www.lintcode.com/problem/1396

// There is a list composed by sets. If two sets have the same elements, merge them. Returns the last remaining collection.

// The number of sets n <=1000.
// The number of elements for each set m <= 100.
// The element must be a non negative integer and not greater than 100000.

// Input:list = [[1],[1,2,3],[4],[8,7,4,5]]
// Output :2
// Explanation:There are 2 sets of [1,2,3] and [4,5,7,8] left.

// Use union find, it automatically deals with solving duplicate and union
// Use the first element of each sets as root
// Time complexity - O(N*M) N - number of sets M - avg number of integers in all sets

class UnionFind {

    Map<Integer, Integer> parents;
    int sizeofSets;

    UnionFind() {
        parents = new HashMap<>();
        sizeofSets = 0;
    }

    void add(int num) {
        if (parents.containsKey(num)) {
            return;
        }

        parents.put(num, null);
        sizeofSets++;
    }

    int find(int num) {

        int root = num;

        while (parents.get(root) != null) {
            root = parents.get(root);
        }

        // 路径压缩
        int current = num;
        while(current != root) {
            int previousParent = parents.get(current);
            parents.put(current, root);
            current = previousParent;
        }
        return root;
    }

    void union(int num1, int num2) {
        int root1 = find(num1);
        int root2 = find(num2);

        if (root1 == root2) {
            return;
        }

        parents.put(root1, root2);
        sizeofSets --;
    }
}

public class Solution {


    /**
     * @param sets: Initial set list
     * @return: The final number of sets
     */
    public int setUnion(int[][] sets) {
        
        UnionFind uf = new UnionFind();
        
        // Write your code here
        if (sets == null || sets.length == 0) {
            return 0;
        }

        for (int i = 0; i < sets.length; i ++) {
            for (int j = 0; j < sets[i].length; j ++) {

                uf.add(sets[i][j]);
                uf.union(sets[i][j], sets[i][0]);
            }        

        }

        return uf.sizeofSets;

    }
}