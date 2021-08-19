// https://www.lintcode.com/problem/444/

// Please design a data structure which can do the following operations:

// void addEdge(int a, int b):add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
// bool isValidTree(): Check whether these edges make up a valid tree.

// 无多边 1->2 2->1 无自环 1->1

// Input:
// addEdge(1, 2)
// isValidTree()
// addEdge(1, 3)
// isValidTree()
// addEdge(1, 5)
// isValidTree()
// addEdge(3, 5)
// isValidTree()
// Output: ["true","true","true","false"]

class UnionFind {

    // Use a hashmap to store the father for each node
    Map<Integer, Integer> father;

    public UnionFind() {
        father = new HashMap<>();
    }

    void add(int num) {

        if (father.containsKey(num)) {
            return;
        }

        father.put(num, null);
    }

    // find the set that this number belongs to
    // A set is identified by the root
    int find(int num) {
        
        int root = num;

        // move upward to the root
        while(father.get(root) != null) {
            root = father.get(root);
        }

        // Path compression! Make it real O(1)
        while (num != root) {
            int originalFather = father.get(num);
            father.put(num, root);
            num = originalFather;
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
        }
    }
}

public class Solution {

    UnionFind uf;
    boolean hasCycle;
    int numOfEdges;

    public Solution() {
        uf = new UnionFind();
        hasCycle = false;
        numOfEdges = 0;
    }

    /**
     * @param a: the node a
     * @param b: the node b
     * @return: nothing
     */
    public void addEdge(int a, int b) {
        uf.add(a);
        uf.add(b);
        numOfEdges++;
        // 如果已经在连通块里了
        if (uf.isConnected(a,b)) {
            hasCycle = true;
        }
        uf.merge(a, b);
    }

    /**
     * @return: check whether these edges make up a valid tree
     */
    public boolean isValidTree() {
        // 1. 点 == 边 + 1
        if (uf.father.size() != numOfEdges + 1) {
            return false;
        }

        // 2. 判断有没有环
        return !hasCycle;
    }
}