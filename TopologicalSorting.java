// https://www.lintcode.com/problem/127/

// Given an directed graph, a topological order of the graph nodes is defined as follow:
// For each directed edge A -> B in graph, A must before B in the order list.
// The first node in the order can be any node in the graph with no nodes direct to it.

// Find any topological order for the given graph.

// graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}

// [0, 1, 2, 3, 4, 5]

// Topological order is only for DAG.

/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     List<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * }
 */

public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {

        // First get in-degree for all node
        // For DAG, there must be nodes with 0 in-degree, and will be the starting
        // points for topological order
        Map<DirectedGraphNode, Integer> indegrees = getInDegrees(graph);

        // Build the queue for BFS
        Queue<DirectedGraphNode> queue = new ArrayDeque<>();

        // Put all starting points into the queue
        for (DirectedGraphNode node : indegrees.keySet()) {
            if (indegrees.get(node) == 0) {
                queue.offer(node);
            }
        }

        // Instead of having a visited hashset, we want to preserve the order
        // of traversal, so we have a list
        ArrayList<DirectedGraphNode> order = new ArrayList<>();

        while (!queue.isEmpty()) {

            DirectedGraphNode node = queue.poll();
            order.add(node);

            for (DirectedGraphNode neighbor : node.neighbors) {

            	// remove the edges from this node to all its neighbors
                indegrees.put(neighbor, indegrees.get(neighbor) - 1);

                if (indegrees.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // If we couldn't exhuast all nodes in the graph, then
        // there could be cycle in the graph. There doesn't exist topological order.
        if (order.size() != graph.size()) {
            return null;
        }

        return order;

    }

    Map<DirectedGraphNode, Integer> getInDegrees(ArrayList<DirectedGraphNode> graph) {

        Map<DirectedGraphNode, Integer> indegrees = new HashMap<>();

        // 先给所有的Node入度为0
        for (DirectedGraphNode node : graph) {
            indegrees.put(node, 0);
        }

        // 能被其他Node access到的入度+1
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegrees.put(neighbor, indegrees.get(neighbor) + 1);
            }
        }

        return indegrees;
    }
}