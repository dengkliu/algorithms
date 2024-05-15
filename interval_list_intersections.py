# https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        p1, p2 = 0, 0

        while p1 < len(firstList) and p2 < len(secondList):
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])

            if start <= end:
                result.append([start, end])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return result  