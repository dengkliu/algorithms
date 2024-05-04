# https://leetcode.com/problems/water-and-jug-problem/description/

# You are given two jugs with capacities x liters and y liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach target using the following operations:

# Fill either jug completely with water.
# Completely empty either jug.
# Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        DIRECTIONS = [x, -x, y, -y] 
        # why do we want a seen set?
        seen = set()
        # why do we need to add 0 to seen here?
        seen.add(0)

        queue = collections.deque()
        queue.append(0)

        while queue:
            total = queue.popleft()
            for delta in DIRECTIONS:
                new_total = total + delta
                if new_total >= 0 and new_total <= x + y:
                    if new_total == target:
                        return True
                    
                    if new_total not in seen:
                        seen.add(new_total)
                        queue.append(new_total)
        
        return False