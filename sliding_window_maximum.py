# https://www.lintcode.com/problem/362/

# Given an array of n integer with duplicate number, and a moving window(size k), 
# move the window at each iteration from the start of the array, 
# find the maximum number inside the window at each moving.

# Input:
# [1,2,7,7,8]
# 3
# 输出:
# [7,7,8]

# Explanation：
# At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
# then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
# then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;

# 1. Brute force 枚举所有区间

# 2. 区间最值问题 用heap

from heapq import heappop, heappush

# 这依然是个min heap
class Heap:
    def __init__(self):
        self.minheap = []
        self.deleted_set = set()
    
    def push(self, index, val):
        heappush(self.minheap, (val, index))

    def _lazy_deletion(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)
    
    def top(self):
        self._lazy_deletion()
        return self.minheap[0]
    
    def pop(self):
        self._lazy_deletion()
        heappop(self.minheap)

    def delete(self, index):
        self.deleted_set.add(index)
    
    def is_empty(self):
        return not bool(self.minheap)

class Solution:

    def __init__(self):
        self.maxheap = Heap()
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        max_values = []

        for i in range(k):
            self.maxheap.push(i, -nums[i])
        
        max_values.append(-self.maxheap.top()[0])
        
        for i in range(len(nums) - k):
            self.maxheap.delete(i)
            self.maxheap.push(i + k, -nums[i + k])
            max_values.append(-self.maxheap.top()[0])
        
        return max_values

# 3. 单调栈