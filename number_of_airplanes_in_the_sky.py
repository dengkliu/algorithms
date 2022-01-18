# https://www.lintcode.com/problem/391/
# Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?
# Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
# Output: 3
# Explanation:
# The first airplane takes off at 1 and lands at 10.
# The second ariplane takes off at 2 and lands at 3.
# The third ariplane takes off at 5 and lands at 8.
# The forth ariplane takes off at 4 and lands at 7.
# During 5 to 6, there are three airplanes in the sky.

# Use scanning line to scan through the timeline
# For starts, add 1
# For ends, substract 1
# Use heap to sort the intervals
# Time complexity O(NlogN)

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Timestamp:
    def __init__(self, flag, value):
        self.flag = flag
        self.value = value

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        time_list = []

        for airplane in airplanes:
            time_list.append(Timestamp(True, airplane.start))
            time_list.append(Timestamp(False, airplane.end))
        
        # Landing should come first before taking off
        time_list.sort(key=lambda time:(time.value, time.flag))

        result = 0
        plane_cnt = 0

        for time in time_list:
            print(time.value)
            if time.flag:
                plane_cnt +=1
                result = max(result, plane_cnt)
            else:
                plane_cnt -=1

        return result