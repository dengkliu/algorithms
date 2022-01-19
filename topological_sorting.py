# https://www.lintcode.com/problem/127/

# Given an directed graph, a topological order of the graph nodes is defined as follow:
# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.

# Find any topological order for the given graph.

# graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}

# [0, 1, 2, 3, 4, 5]

# Topological order is only for DAG.

"""
 Definition for Directed graph.

 class DirectedGraphNode:
    def __init__(self, neighbors, x):
        self.label = x
        self.neighbors = []
"""

public class Solution {
    """
    @param graph: A list of Directed graph node
     @return: Any topological order for the given graph.
    """
    def topSort(self, graph):

        # First get in-degree for all node
        # For DAG, there must be nodes with 0 in-degree, and will be the starting
        # points for topological order
        indegrees = self.__get_indegrees(graph)

        for node, indegree in indegrees.items():
            if indegree == 0:
            queue.append(node)

        # Instead of having a visited hashset, we want to preserve the order
        # of traversal, so we have a list
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.offer(neighbor)

        if len(order) != len(graph):
            return None

        return order
    }

    def __get_indegrees(self, graph):
        indegrees = {}

        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1

        return indegrees