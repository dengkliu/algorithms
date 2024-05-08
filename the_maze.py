# https://leetcode.com/problems/the-maze/
# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it # won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the 
# ball can stop at the destination, otherwise return false.
# You may assume that the borders of the maze are all walls (see examples).

class MazeGridType:
    SAPCE = 0
    WALL = 1

class Solution(object):
    def hasPath(self, maze, start, destination):
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
        visited = {start}

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()
            for row_delta, col_delta in direction:
                row_next, col_next = kickball(row, col, row_delta, col_delta, maze, destination)
              
                if (row_next, col_next) == destination:
                    return True

                if (row_next, col_next) in visited:
                    continue
                    
                visited.add((row_next, col_next))
                queue.append((row_next, col_next))

        return False
