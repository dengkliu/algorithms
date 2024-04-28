# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

# You are given an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# You are also given a 0-indexed integer array cost of length n, where cost[i] is the cost assigned to the ith node.
# You need to place some coins on every node of the tree. The number of coins to be placed at node i can be calculated as:

# If size of the subtree of node i is less than 3, place 1 coin.
# Otherwise, place an amount of coins equal to the maximum product of cost values assigned to 3 distinct nodes in the subtree of node i. If this product is negative, place 0 coins.
# Return an array coin of size n such that coin[i] is the number of coins placed at node i.

class Solution(object):
    def placedCoins(self, edges, cost):
        """
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: List[int]
        """
        if not cost:
            return []

        n = len(cost)
        coin = [0] * n
        graph = collections.defaultdict(set)
        for v, u in edges:
            graph[v].add(u)
            graph[u].add(v)

        def dfs(root, parent):

            costs = [cost[root]]

            for child in graph[root]:
                if child != parent:
                    costs += dfs(child, root)

            if len(costs) < 3:
                coin[root] = 1
            else:
                costs.sort()
                max_coin = max(0, costs[0] * costs[1] * costs[-1], costs[-1] * costs[-2] * costs[-3])
                coin[root] = max_coin 
            
            return costs

        dfs(0, None)
        return coin