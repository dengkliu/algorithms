# https://leetcode.com/problems/detonate-the-maximum-bombs/

# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

class Solution(object):
    # Why union find is not an option here?
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)

        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if pow(xi - xj, 2) + pow(yi - yj, 2) <= pow(ri, 2):
                    graph[i].add(j)

        result = [1]

        def bfs(i):
            queue = collections.deque()
            visited = set()
            queue.append(i)
            visited.add(i)

            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in visited:
                        queue.append(y)
                        visited.add(y)
            
            result[0] = max(result[0], len(visited))

        for i in range(n):
            bfs(i)           
                        
        return result[0]