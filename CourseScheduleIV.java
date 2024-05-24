// https://www.lintcode.com/problem/815
// There are a total of n courses you have to take, labeled from 0 to n - 1.
// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
// which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, 
// return the number of different ways you can get all the lessons.
// Input:
// n = 2
// prerequisites = [[1,0]]
// Output: 1
// Explantion:
// You must have class in order 0->1.

// 拓扑排序 + DFS
// 拓扑排序的核心思想 --> 
// 访问一个点，把这个点标记为访问，并且所有这个点的child indgree都减一 假如某个child的indegree为0了 就可以入队访问了

// DFS -> 在每一层，能够访问的就是indegree是0的点
// 对于当前层 一次对每个入度为0的点进行DFS 标记为访问 并且有这个点的child indgree都减一
// 然后进入下一层 下一层将访问在下一层入度为0的点
// 为了避免重复访问 用一个set 或者array记录已经访问的点
public class Solution {

    int result = 0;

    /**
     * @param n: an integer, denote the number of courses
     * @param p: a list of prerequisite pairs
     * @return: return an integer,denote the number of topologicalsort
     */
    public int topologicalSortNumber(int n, int[][] p) {

       int[] indegree = new int[n];
       
       Map<Integer, Set<Integer>> graph = buildGraph(p, n, indegree);
       
       boolean[] visited = new boolean[n];
        
        dfs(0, graph, indegree, visited, n);

        return result;
    }

    Map<Integer, Set<Integer>> buildGraph(int[][] prerequisites, 
        int n, int[] indegree) {

        Map<Integer, Set<Integer>> graph = new HashMap<>();

        for (int i = 0; i < n; i ++) {
            graph.put(i, new HashSet<>());
        }

        for(int[] prerequisite : prerequisites) {
            int start = prerequisite[1];
            int end = prerequisite[0];
            if (graph.get(start).contains(end)) {
                continue;
            }
            graph.get(start).add(end);
            indegree[end] ++;;
        }

        return graph;
    }

    // 每次深入一层 改变的参数是set要新加一个数 
    // 这个时候 如果set已经有这个数了 说明出现了环 直接返回
    // 如果加入之后 set size达到了数目 就说明找到了一个路径
    void dfs(int visitedCnt, Map<Integer, Set<Integer>> graph, 
                int[] indegree, boolean[] visited, int n) {

        if (visitedCnt == n) {
            result ++;
        }

        for (int i = 0; i < n; i ++) {
            // 拓扑排序的核心思想 - 只有当Indegree为0的时候 才能入队！！
            // 假如不存在拓扑排序 那么在某一层 根本就找不到入度为0的点
            // 根本访问不到所有节点！
            // 只要能访问到所有节点 就一定存在拓扑排序！
            if (!visited[i] && indegree[i] == 0) {
                visited[i] = true;
                for (int next : graph.get(i)) {
                    indegree[next] --;
                }
                dfs(visitedCnt + 1, graph, indegree, visited, n);
                for (int next : graph.get(i)) {
                    indegree[next] ++;
                }
                visited[i] = false;
            }
        }
    }
}