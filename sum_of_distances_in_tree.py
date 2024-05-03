# https://leetcode.com/problems/sum-of-distances-in-tree/description/

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.


class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        # undirected graph
        for u, v in edges:
            graph[v].add(u)
            graph[u].add(v)
        
        # we need to use this in dfs2()
        # so we memorize it
        subtree_size = [0] * n
        
        def dfs(node, parent):
            curr_dist = 0
            curr_tree_size = 1
            for child in graph[node]:
                # dfs for undiret graph, we have to make sure we don't do redunbant traversal
                if child != parent:
                    child_dist = dfs(child, node)
                    curr_dist +=  child_dist + subtree_size[child]
                    curr_tree_size += subtree_size[child]
            subtree_size[node] = curr_tree_size
            return curr_dist
        
        root_dist = dfs(0, None)
    
        result = [0] * n
        result[0] = root_dist

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # ans[x] = x@x + y@y + size[y]
                    # ans[y] = x@x + y@y + size[x]
                    # ans[x] = ans[y] + size[y] - size[x]
                    result[child] = result[node] + (n - subtree_size[child]) - subtree_size[child]
                    dfs2(child, node)

        dfs2(0, None)
        
        return result
        