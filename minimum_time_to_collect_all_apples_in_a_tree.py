# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [False for i in range(n)]
        min_time = [0]

        # why do we use post order?
        def dfs(root):
            visited[root] = True
            appleFound = False
            for child in graph[root]:
                if not visited[child]:
                    # why do we put dfs(child) first
                    appleFound = dfs(child) or appleFound

            if not appleFound:
                appleFound = hasApple[root]

            if appleFound and root != 0:
                min_time[0] += 2
                
            return appleFound

        dfs(0)
        
        return min_time[0]



