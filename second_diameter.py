# Given a tree consisting of n nodes, n-1 edges. 
# Output the second diameter of a tree, namely, the second largest value of distance between pairs of nodes.
# Given an array edge of size (n−1)×3, 
# and edge[i][0], edge[i][1] and edge[i][2] indicate that the i-th undirected edge is 
# from edge[i][0] to edge[i][1] and the length is edge[i][2].

# Input:[[0,1,4],[0,2,7]]
# Output:7
# Explanation: The second largest value of distance is 7 between node 0 and node 2.

class Solution:
    """
    @param edge: edge[i][0] [1] [2]  start point,end point,value
    @return: return the second diameter length of the tree
    """
    def getSecondDiameter(self, edge):
        
        graph = self.build_graph(edge)
        
        first_end = 0
        
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
                    first_end = neighbor

        queue.clear()
        distance.clear()

        queue.append(first_end)
        distance = {first_end : 0}

        max_distance = - float('inf')
        second_end = 0

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
                    second_end = neighbor

        
        second_diameter = - float('inf')

        queue.clear()
        distance.clear()
        queue.append(first_end)
        distance = {first_end : 0}

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in distance or neighbor == second_end :
                    continue
                # 加到queue里    
                queue.append(neighbor)
                # 更新distance
                distance[neighbor] = distance[node] + graph[node][neighbor]
                if distance[neighbor] > second_diameter:
                    second_diameter = distance[neighbor]

        queue.clear()
        distance.clear()
        queue.append(second_end)
        distance = {second_end : 0}

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in distance or neighbor == first_end :
                    continue
                # 加到queue里    
                queue.append(neighbor)
                # 更新distance
                distance[neighbor] = distance[node] + graph[node][neighbor]
                if distance[neighbor] > second_diameter:
                    second_diameter = distance[neighbor]

        return second_diameter

    
    def build_graph(self, edge):
        n = len(edge)
        graph = { i : {} for i in range(n + 1)}
        for e in edge:
            graph[e[0]][e[1]] = e[2]
            graph[e[1]][e[0]] = e[2]
            
        return graph
