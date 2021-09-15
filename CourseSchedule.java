// There are a total of n courses you have to take, labeled from 0 to n - 1.
// Before taking some courses, you need to take other courses. 
// For example, to learn course 0, you need to learn course 1 first, which is expressed as [0,1].
// Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

// Input: n = 2, prerequisites = [[1,0]] 
// Output: true

// 典型的拓扑排序问题 要验证有向无环图

public class Solution {
    /**
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        Map<Integer, Integer> indegree = new HashMap<>();

        Map<Integer, Set<Integer>> graph = buildGraph(prerequisites, numCourses, indegree);

        Queue<Integer> queue = new ArrayDeque<>();

        Set<Integer> visited = new HashSet<>();

        for (int i = 0; i < numCourses; i ++) {
            if (indegree.get(i) == 0) {
                queue.add(i);
            }
        }

        while(!queue.isEmpty()) {
            int curr = queue.poll();
            visited.add(curr);

            for (int next : graph.get(curr)) {
                indegree.put(next, indegree.get(next) - 1);         
                if (indegree.get(next) == 0) {
                    queue.offer(next);
                }
            }
        }

        return visited.size() == numCourses;
    }

    Map<Integer, Set<Integer>> buildGraph(int[][] prerequisites, 
        int numCourses, Map<Integer, Integer> indegree) {

        Map<Integer, Set<Integer>> graph = new HashMap<>();

        for (int i = 0; i < numCourses; i ++) {
            graph.put(i, new HashSet<>());
            indegree.put(i, 0);
        }

        for(int[] prerequisite : prerequisites) {
            int start = prerequisite[1];
            int end = prerequisite[0];
            if (graph.get(start).contains(end)) {
                continue;
            }
            graph.get(start).add(end);
            indegree.put(end, indegree.get(end) + 1);
        }

        return graph;
    }
}