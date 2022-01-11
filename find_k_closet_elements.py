# https://www.lintcode.com/problem/460/
# Given target, a non-negative integer k and an integer array A sorted in ascending order, 
# find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
# Otherwise, sorted in ascending order by number if the difference is same.

# The value k is a non-negative integer and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^4
# Absolute value of elements in the array will not exceed 10^4

# Input: A = [1, 2, 3], target = 2, k = 3
# Output: [2, 1, 3]

# Brute and force: 计算每个数字和target的difference
# 然后跟据difference排序，可以用heap 但是复杂度度是 N*logN + K

# 可以用二分法 因为数组是sorted 可以找到离target最近的数
# 然后用two pointer向两边找次近的数
# 复杂度是 logN + K

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):

        result = []

        if not A:
            return result
        # write your code here
        closest_num_index = self.binary_search(A, target)

        print(closest_num_index)

        left, right = closest_num_index, closest_num_index + 1

        while left >= 0 and right < len(A):
            left_distance = target - A[left]
            right_distance = A[right] - target

            if len(result) == k:
                return result
            elif left_distance > right_distance:
                result.append(A[right])
                right += 1
            else:
                result.append(A[left])
                left -=1
        
        while left >=0 and len(result) < k:
            result.append(A[left])
            left -=1
        
        if len(result) == k:
            return result
       
        while right < len(A) and len(result) < k:
            result.append(A[right])
            right+=1
          
        return result

    def binary_search(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                end = mid

        if target - A[start] > A[end] - target:
            return end
        else:
            return start