# https://leetcode.com/problems/minimum-height-trees/

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# This is using topological sort
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        graph = collections.defaultdict(set)
        # Why do we need a connection array?
        connections = [0] * n
        # how to initialze a set of numbers from 0 to n-1
        nodes = set(range(n))

        for u, v in edges:
            connections[u] += 1
            connections[v] += 1
            graph[u].add(v)
            graph[v].add(u)
        
        queue = collections.deque()
        # why do we need a visited list here?
        visited = []

        for i in range(n):
            if connections[i] == 1:
                # Add leaf nodes
                queue.append(i)
                visited.append(i)

        while queue:
            # why do we need to process entire level?
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                # remove this node because it's a leaf
                nodes.remove(curr)
                for child in graph[curr]:
                    if child not in visited:
                        connections[child] -= 1
                        # check if it's a leaf node
                        if connections[child] == 1:
                            queue.append(child)
                            visited.append(child)
            if len(nodes) <= 2:
                break

        return nodes

