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

        def dfs(total):
            for delta in DIRECTIONS:
                new_total = total + delta
                if new_total >= 0 and new_total <= x + y:
                    if new_total == target:
                        return True
                    else:
                        # why do we want to skip seen?
                        if new_total not in seen:
                            seen.add(new_total)
                            # remember to return here!
                            return dfs(new_total)

        return dfs(0)