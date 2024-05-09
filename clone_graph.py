# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # what is shallow copy and what is deep copy 
        def dfs(node, visited):

            if not node:
                return None 
            
            # why do we need a map from node to copy node?
            if node in visited:
                return visited[node]

            copy = Node(node.val, [])
            visited[node] = copy

            for n in node.neighbors:
                n_copy = dfs(n, visited)
                copy.neighbors.append(n_copy)

            return copy

        visited = {}
        
        return dfs(node, visited)