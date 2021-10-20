# https://www.lintcode.com/problem/510/

# Given a 2D boolean matrix filled with False and True, 
# find the largest rectangle containing all True and return its area.

# Input:
# [
#  [1, 1, 0, 0, 1],
#  [0, 1, 0, 0, 1],
#  [0, 0, 1, 1, 1],
#  [0, 0, 1, 1, 1],
#  [0, 0, 0, 0, 1]
# ]
# Output: 6

class Solution:

    def __init__(self):
        self.max_area = 0
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        heights = [0 for _ in range(len(matrix[0]))]

        row_count = len(matrix)
        col_count = len(matrix[0])

        for row in range(row_count - 1):
            for col in range(col_count): 
                if not matrix[row][col]:
                    # reset 到 0
                    heights[col] = 0
                    continue
                heights[col] += 1

            self.get_max_area(heights, row_count, col_count)

        for col in range(col_count):
            if not matrix[row_count -1][col]:
                heights[col] = 0
                continue
            heights[col] += 1
        
        self.get_max_area(heights, row_count, col_count)

        return self.max_area

    def get_max_area(self, heights, row_count, col_count):
        
        stack = []

        for i in range(col_count + 1):
            new_height = -1 if i == col_count else heights[i]
            
            while stack and heights[stack[-1]] >= new_height:
                index = stack.pop(-1)
                curr_height = heights[index]
                prev_index = stack[-1] if stack else -1
                self.max_area = max(self.max_area, curr_height * (i - prev_index - 1))
                
            stack.append(i)
