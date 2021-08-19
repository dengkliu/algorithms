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

public class Solution {

	UnionFind uf;
	boolean hasCycle;
	int numOfEdges;

    /**
     * @param a: the node a
     * @param b: the node b
     * @return: nothing
     */
    public void addEdge(int a, int b) {
        // write your code here
    }

    /**
     * @return: check whether these edges make up a valid tree
     */
    public boolean isValidTree() {
        // write your code here
    }
}
