# https://leetcode.com/problems/tree-diameter/

# The diameter of a tree is the number of edges in the longest path in that tree.

# There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

# Return the diameter of the tree.


class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        result = [0]

        def dfs(root, parent):
            child_cnt = 0
            # maintain 2 maximum child path
            top_1_path = 0
            top_2_path = 0
            for child in graph[root]:
                if child != parent:
                    child_cnt += 1
                    child_path = dfs(child, root)
                    # how do we update the 2 maximum paths
                    if child_path > top_1_path:
                        top_2_path = top_1_path
                        top_1_path = child_path
                    elif child_path > top_2_path:
                        top_2_path = child_path
            
            if child_cnt == 0:
                return 0
            elif child_cnt == 1:
                result[0] = max(result[0], top_1_path + 1)
                return top_1_path + 1
            elif child_cnt >= 2:
                result[0] = max(result[0], top_1_path + 1 + top_2_path + 1)
                return top_1_path + 1
        
        dfs(0, -1)

        return result[0]