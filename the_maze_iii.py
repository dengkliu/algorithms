# https://www.lintcode.com/problem/789/

# There is a ball in a maze with empty spaces and walls. 
# The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. 
# When the ball stops, it could choose the next direction. 
# There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

# Given the position of the ball, the position of the hole and the maze, 
# find out how the ball falls into the hole by moving the shortest distance. 
# The distance is defined by the number of empty spaces the ball passes from the starting position (excluded) to the hole (included). 
# Use "u", "d", "l" and "r" to output the direction of movement. 
# Since there may be several different shortest paths, you should output the shortest method in alphabetical order.
# If the ball doesn't go into the hole, output "impossible".

# The maze is represented by a binary 2D array. 
# 1 means the wall and 0 means the empty space. 
# You may assume that the borders of the maze are all walls. 
# The ball and the hole coordinates are represented by row and column indexes.

# Input:
# [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
# [4,3]
# [0,1]

# Output: "lul"

class MazeGridType:
    SAPCE = 0
    WALL = 1

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """

        if not ball or not hole or not maze or not maze[0]:
            return 'impossible'

        queue = collections.deque()
        queue.append((ball[0], ball[1]))
        distance = {(ball[0], ball[1]) : 0}
        path = {(ball[0], ball[1]) : ''}
        hole = (hole[0], hole[1])

        def is_wall(row, col, maze):
            if row < 0 or row >= len(maze):
                return True

            if col < 0 or col >= len(maze[0]):
                return True

            if maze[row][col] == MazeGridType.WALL:
                return True

        def kickball(row, col, d_row, d_col, maze, hole):            
            while (row, col) != hole and not is_wall(row, col, maze):
                row = row + d_row
                col = col + d_col

            if (row, col) == hole:
                return hole

            row = row - d_row
            col = col - d_col

            return (row, col)

        while queue:
            row, col = queue.popleft()

            for d_row, d_col, step in ((1, 0, 'd'),  (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')):
                adj_row, adj_col = kickball(row, col, d_row, d_col, maze, hole)
                new_distance = distance[(row, col)] + abs(adj_row - row) + abs(adj_col - col)
                new_path =  path[(row, col)] + step

                if (adj_row, adj_col) in distance:
                    if distance[(adj_row, adj_col)] < new_distance:
                        continue
                    if distance[(adj_row, adj_col)] == new_distance and path[(adj_row, adj_col)] <= new_path:
                        continue
                
                queue.append((adj_row, adj_col))
                distance[(adj_row, adj_col)] = new_distance
                path[(adj_row, adj_col)] = path[(row, col)] + step

        if hole in path:        
            return path[hole]

        return 'impossible'





