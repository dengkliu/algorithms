# https://leetcode.com/problems/buildings-with-an-ocean-view/

# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        if not heights:
            return stack

        stack.append(0)

        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)

        return stack