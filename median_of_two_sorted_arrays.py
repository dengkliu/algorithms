# https://leetcode.com/problems/median-of-two-sorted-arrays/
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log(m + n)).

# Fundelmentals 
# For an array of length N -
# If N is odd, then median is A[N/2]
# If N is even, then medain is (A[N/2-1] + A[N/2])/2

# test case: [1] [0, 3]; [1, 2] [3, 4]; [] [2, 3]

# 题眼：
# 1. 二分的是A数组数目的个数，而不是index;因为个数有可能是0。假如用index，index最小取到0，相当于一直默认A数组一定有至少数字在最终的4个数里面。但是显然这是不对的 - 当A数组的所有数字都小于B数组的最小数字的时候。
# 2. 很tricky - 循环结束判定条件是 start <= end 两者要merge 然后更新的时候要用start = mid + 1 和 end = mid - 1 不然会陷入死循环
# 3. 记得最后的除法用浮点

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # For an array of length N -
        # If N is odd, then median is A[N/2]
        # If N is even, then medain is (A[N/2-1] + A[N/2])/2

        # For this problem, we want to keep (N + M)//2 numbers on the left
        # We want to do the cut so that -
        # maxLeftA <= minRightB
        # maxRightA => minLeftB
        # so we make sure the median of the marged array would be included in these 4 numbers

        N1, N2 = len(nums1), len(nums2)

        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)

        if N1 == 0:
            return (nums2[N2//2-1] + nums2[N2//2])/2.0 if N2%2 == 0 else nums2[N2//2]

        
        # [1, 2, inf]
        # [-inf, 3, 4]
        # how many numbers we want to include from nums1
        start, end = 0, N1

        while start <= end:
            mid = (start + end)//2
            L1 = float('-inf') if mid - 1 < 0 else nums1[mid - 1]
            R1 = float('inf') if mid >= N1 else nums1[mid]
            L2 = float('-inf') if (N1 + N2)//2 - mid - 1 < 0 else nums2[(N1 + N2)//2 - mid - 1]
            R2 = float('inf') if (N1 + N2)//2 - mid >= N2 else nums2[(N1 + N2)//2 - mid]

            if L1 > R2:
                end = mid - 1
            elif L2 > R1:
                start = mid + 1
            else:
                if (N1 + N2)%2 == 0:
                    return (max(L1, L2) + min(R1, R2))/2.0
                else:
                    return min(R1, R2)
        
        return -1
