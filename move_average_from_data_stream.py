# https://leetcode.com/problems/moving-average-from-data-stream/

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
# MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.nums = collections.deque()
        # why use float?
        self.sum = float(0)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        self.sum += val
        if len(self.nums) > self.size:
            self.sum -= self.nums[0]
            self.nums.popleft()
            return self.sum/self.size
        else:
            return self.sum/len(self.nums)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


