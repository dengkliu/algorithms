# https://leetcode.com/problems/k-closest-points-to-origin/description/

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        
        for x, y in points:
            distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(heap, (distance, (x, y)))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans