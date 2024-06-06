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

    old_to_new = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:

        if node in self.old_to_new:
            return self.old_to_new[node]
        
        copy = Node(node.val)
        self.old_to_new[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(self.cloneGraph(nei))

        return copy