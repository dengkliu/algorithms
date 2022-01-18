# https://www.lintcode.com/problem/404/
# Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.

# Input: A = [1, 2, 3, 4], start = 1, end = 3
# Output: 4
# Explanation: All possible subarrays: [1](sum = 1), [1, 2](sum = 3), [2](sum = 2), [3](sum = 3).

# Prefix sum
# Two pointers.

class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):

        #    [1, 2, 3, 4, 5] interval 0 0
        # [0, 1, 3, 6, 10, 15]
        #

        prefix_sum = [0 for i in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]
        
        left, right = 0, 0

        result = 0

        for index in range(1, len(A) + 1):

            # move the left until the subarray sum <= end
            # 
            while left < index and prefix_sum[index] - prefix_sum[left] > end:
                left += 1

            while right < index and prefix_sum[index] - prefix_sum[right] >= start:
                right += 1
            
            result += right - left
        
        return result