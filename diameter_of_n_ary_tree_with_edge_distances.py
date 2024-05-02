# Given a tree consisting of n nodes, n-1 edges. O
# utput the distance between the two nodes with the furthest distance on this tree.
# Given three arrays of size n-1, starts, ends, and lens, indicating that the i-th edge is from starts[i] to ends[i] and the length is lens[i].

#  Return the farthest distance between any two nodes on the tree, not the depth of the tree. 
#  Note that the given edges are undirected edge.
#  It is guaranteed that the given edges are able to constitute a tree.

#  1 <= n <= 1*10^5
# 1 <= lens[i] <= 1*10^3

#  两次BSF
#  1. 随便选一个起点，找到离这个起点最远的点
#  2. 再从这个最远的出发，找到离这个点最远的点

class Solution:


    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        
        graph = self.build_graph(starts, ends, lens, n)

        max_node = 0
        max_distance = - float('inf')

        queue = collections.deque([0])
        distance = {0: 0}

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in distance:
                    continue
                # 加到queue里    
                queue.append(neighbor)
                # 更新distance
                distance[neighbor] = distance[node] + graph[node][neighbor]
                if distance[neighbor] > max_distance:
                    max_distance = distance[neighbor]
                    max_node = neighbor

        queue.clear()
        distance.clear()
        
        queue.append(max_node)
        distance = {max_node : 0}
        max_distance = - float('inf')

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in distance:
                    continue
                queue.append(neighbor)
                distance[neighbor] = distance[node] + graph[node][neighbor]
                if distance[neighbor] > max_distance:
                    max_distance = distance[neighbor]

        return max_distance       

    
    def build_graph(self, starts, ends, lens, n):
        # python不好定义set
        # 用双层dictionary来代替吧
        graph = {i:{} for i in range(n)}
        for i in range(len(starts)):
            graph[starts[i]][ends[i]] = lens[i]
            graph[ends[i]][starts[i]] = lens[i]
        return graph

        
