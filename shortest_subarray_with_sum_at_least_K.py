# https://www.lintcode.com/problem/1507/

# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

# If there is no non-empty subarray with sum at least K, return -1.

# 1 <= A.length <= 50000
# -10^5 <= A[i] <= 10^5
# 1 <= K <= 10

# Input: A = [1], K = 1
# Output: 1

# [1 2 -1 -6 5 6]  K = 5
# 0 2 3 2 -4 1 7

class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        
        if not A or K == 0:
            return 0

        prefix_sum = self.__get_prefix_sum(A)

        # initialize queue in python
        deq = collections.deque()

        min_length = float('inf')
        
        # 单调递增栈
        # 栈首的元素一定是前面的元素里最小的
        # 那么用当前的元素减去前面的元素 一定是最大的 和K作比较
        # 假如比K大 那么还可以往里面收 让区间越小越好
        for i in range(len(prefix_sum)):
            curr_sum = prefix_sum[i]
            # 去掉比当前大的prefix sum
            # 不用考虑 当前的位置更靠后 还更小 肯定能和后面组成更小的但和更大的区间
            while deq and prefix_sum[deq[-1]] > curr_sum:
                deq.pop()

            # 队首的是最小的prefix sum 看看区间和是不是大于K
            # 如果大于的话 可以缩小
            while deq and (curr_sum - prefix_sum[deq[0]] >= K):
                min_length = min(min_length, i - deq[0])
                deq.popleft()

            deq.append(i)

        return min_length if min_length != float('inf') else -1

    def __get_prefix_sum(self, A):
        prefix_sum = [0 for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        return prefix_sum
