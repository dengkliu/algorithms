# https://www.lintcode.com/problem/1219

# Winter is coming! Your first job during the contest is to design a standard heater
# with fixed warm radius to warm all the houses.
# Now, you are given positions of houses and heaters on a horizontal line, 
# find out minimum radius of heaters so that all houses could be covered by those heaters.
# So, your input will be the positions of houses and heaters seperately, 
# and your expected output will be the minimum radius standard of heaters.

# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, 
# and if we use the radius 1 standard, then all the houses can be warmed.

# 基本想法：
# 1. 针对每个加热器 找到所有可以找它加热的房子。这样对于每个房子，需要比较这个加热器和其他加热器到房子的距离，不方便。
# 2. 针对每个房子 找到离其最近的加热器 这样才能节省加热器的距离。对于每个房子，不用考虑其他房子，只考虑它自己就好了。

# 解法
# 1. Binary search
#    针对一个target 找到数组里离它最近的一个数 可以用二分法

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):

        heaters.sort()

        result = float('-inf')
        # Write your code here
        for house in houses:
            heater = self.__find_nearest_heaters(house, heaters)
            distance = heater - house
            radius_for_house = distance if distance > 0 else - distance
            result = max(result, radius_for_house)
        return result
    
    def __find_nearest_heaters(self, house, heaters):
        start, end = 0, len(heaters) - 1

        while start + 1 < end:
            mid = (start + end)//2
            if heaters[mid] > house:
                end = mid
            else:
                start = mid

        distance_to_start = house - heaters[start]
        distance_to_end = heaters[end] - house

        return heaters[start] if distance_to_start < distance_to_end else heaters[end] 