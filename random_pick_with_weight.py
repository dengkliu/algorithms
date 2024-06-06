# https://leetcode.com/problems/random-pick-with-weight/

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sum = [0 for _ in range(len(w))]
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] += w[i] + self.prefix_sum[i - 1]
            
    def binary_search(self, arr, x):
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < x:
                start = mid + 1
            else:
                end = mid

        return start

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(1, self.prefix_sum[-1])
        index = self.binary_search(self.prefix_sum, x)
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
