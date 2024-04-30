# https://leetcode.com/problems/graph-valid-tree/description/

# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(root, parent, visited):
            isValid = True
            for child in graph[root]:
                if child != parent:
                    if child in visited:
                        return False
                    else:
                        visited.append(child)
                        isValid = isValid and dfs(child, root, visited)
            return isValid
        
        visited = [0]
        # why do we need to check both?
        return dfs(0, -1, visited) and len(visited) == n