# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda interval:(interval[0], interval[1]))

        res = [intervals[0]]
        
        for index in range(1, len(intervals)):
            interval = intervals[index]
            start = res[-1][0]
            end = res[-1][1]
            if end >= interval[0]:
                # perform the merge
                res[-1][1] = max(end, interval[1])
            else:
                res.append(interval)

        return res