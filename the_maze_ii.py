# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it # won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see examples).

class MazeGridType:
    SAPCE = 0
    WALL = 1

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        def kickball(row, col, row_delta, col_delta, maze, destination):
            while not is_wall(row, col, maze):
                row = row + row_delta
                col = col + col_delta

            row = row - row_delta
            col = col - col_delta
            return (row, col)

        
        def is_wall(row, col, maze):
            if row < 0 or row >= len(maze):
                return True
            if col < 0 or col >= len(maze[0]):
                return True
            
            return maze[row][col] == MazeGridType.WALL

        if not maze or not start or not destination or not maze[0]:
            return -1    

        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        queue = collections.deque()
        queue.append(start)
        distance = {start: 0}

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()
            for row_delta, col_delta in direction:
                row_next, col_next = kickball(row, col, row_delta, col_delta, maze, destination)
                new_distance = distance[(row, col)] + abs(row_next - row) + abs(col_next - col)

                if (row_next, col_next) in distance and distance[(row_next, col_next)] <= new_distance:
                    continue
                    
                distance[(row_next, col_next)] = new_distance
                queue.append((row_next, col_next))

        if destination in distance:
            return distance[destination]

        return -1

