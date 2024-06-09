# https://leetcode.com/problems/kth-missing-positive-number/

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # [1, 2, 3, 4, 5]
        # [2, 3, 4, 7, 11]
        # [1, 1, 1, 3, 6]
        # 7 + 5 - (7 - 4)
        # missing_num_cnt = arr[index] - (index + 1)
        low, high = 0, len(arr) - 1

        while low <= high:
            middle = (low + high) // 2
            if arr[middle] - middle - 1 < k:
                low = middle + 1
            else:
                high = middle - 1
        
        # At the end of the loop, low = high + 1,
        # and the kth missing is in-between arr[low] and arr[right].
        # The number of integers missing before arr[low] is
        # arr[low] - low - 1 -->
        # the number to return is
        # arr[low] + k - (arr[low] - low - 1) = k + low
        return low + k