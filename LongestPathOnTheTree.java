// Given a tree consisting of n nodes, n-1 edges. O
// utput the distance between the two nodes with the furthest distance on this tree.
// Given three arrays of size n-1, starts, ends, and lens, indicating that the i-th edge is from starts[i] to ends[i] and the length is lens[i].

// Return the farthest distance between any two nodes on the tree, not the depth of the tree. 
// Note that the given edges are undirected edge.
// It is guaranteed that the given edges are able to constitute a tree.

// 1 <= n <= 1*10^5
// 1 <= lens[i] <= 1*10^3

// 两次BSF
// 1. 随便选一个起点，找到离这个起点最远的点
// 2. 再从这个最远的出发，找到离这个点最远的点

public class Solution {
    /**
     * @param n: The number of nodes
     * @param starts: One point of the edge
     * @param ends: Another point of the edge
     * @param lens: The length of the edge
     * @return: Return the length of longest path on the tree.
     */
    public int longestPath(int n, int[] starts, int[] ends, int[] lens) {

        Map<Integer, Set<int[]>> tree = buildTree(starts, ends, lens);

        Queue<Integer> queue = new ArrayDeque<>();

        // 存放到起点的距离
        Map<Integer, Integer> distances = new HashMap<>();

        // 随便选一个起点
        queue.add(starts[0]);
        distances.put(starts[0], 0);

        int maxDistance = Integer.MIN_VALUE;
        int maxNode = 0;

        while(!queue.isEmpty()) {

            int curr = queue.poll();

            Set<int[]> kids = tree.get(curr);

            if (kids == null) {
                continue;
            }

            for (int[] next : kids) {
                int nextNode = next[0];
                int edgeLength = next[1];
                if (distances.containsKey(nextNode)) {
                    continue;
                }

                queue.add(nextNode);
                int newDistance = distances.get(curr) + edgeLength;
                distances.put(nextNode, newDistance);

                if (newDistance > maxDistance) {
                    maxDistance = newDistance;
                    maxNode = nextNode;
                }
            }
        }

        // System.out.println("Max distance: " + maxDistance);
        // System.out.println("Max node: " + maxNode);

        queue.clear();
        distances.clear();
        maxDistance = Integer.MIN_VALUE;

        queue.add(maxNode);
        distances.put(maxNode, 0);

        while(!queue.isEmpty()) {

            int curr = queue.poll();

            Set<int[]> kids = tree.get(curr);

            if (kids == null) {
                continue;
            }

            for (int[] next : kids)  {
                int nextNode = next[0];
                int edgeLength = next[1];
                if (distances.containsKey(nextNode)) {
                    continue;
                }

                queue.add(nextNode);
                int newDistance = distances.get(curr) + edgeLength;
                distances.put(nextNode, newDistance);

                if (newDistance > maxDistance) {
                    maxDistance = newDistance;
                }
            }
        }

        return maxDistance;
    }


    Map<Integer, Set<int[]>> buildTree(int[] starts, int[] ends, int[] lens) {

        Map<Integer, Set<int[]>> tree = new HashMap<>();

        for (int i = 0; i < starts.length; i ++) {

            int start = starts[i];
            int end = ends[i];

            Set<int[]> set = tree.getOrDefault(start, new HashSet<>());
            set.add(new int[]{end, lens[i]});
            tree.put(start, set);

            // 要加双向！
            Set<int[]> endSet = tree.getOrDefault(end, new HashSet<>());
            endSet.add(new int[]{start, lens[i]});
            tree.put(end, endSet);
        }

        return tree;
    }

}