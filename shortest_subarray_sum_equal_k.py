
# https://www.lintcode.com/problem/1844/
# Given an array of integers and an integer k, 
# you need to find the minimum size of continuous no-empty subarrays whose sum equals to k, and return its length.
# if there are no such subarray, return -1.

# Input: nums = [1,1,1,2] and k = 3
# Output: 2 = 1 + 2

# 1. Brute Force - enumerate the start and end of the subarray, 
#    calculate the sum for each of them, and check if it is K。 It is going to be O(N^3)
#    for (int start = 0; start < n; start ++) {
#        for (int end = start + 1; end < n; end ++) {
#             for (int k = start; k < end; k ++) {
#             }
#        }
#    }
# 2. Calculate Prefix Sum beforehand. Don't need to calculate the sum of subarray again.
#    Still need to enumerate the start and end of the subarray. There are N^2 combinations
#    O(N^2)
# 3. Let's think in this way. We just need to enumerate the end. The start must be at the index
#    which make sure that prefixSum[end] - prefixSum[start -1] is the K. We don't have length constraints here, so the start 
#    can be from 0 to end - 1. We can keep tracking the subarray length.
#    How do we find prefixSum[start-1] in O(1) time? We can use hashmap. Hashmap checks key existance in O(1) time
#    So we can have a hashmap with sum to index pair. 
#    We enumerate the end from index 0 to n-1, for each one we look up the hashmap. 
#    This can be done in O(N)

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        if not nums:
            return -1

        # prefix sum array 的长度比nums长度多一个
        #   1 2
        # 0 1 3
        prefix_sum = 0

        index_to_prefix_sum = {}
        # prefix sum to index map, the sum includes the current index
        index_to_prefix_sum[0] = -1

        result = float('inf')

        for i in range(1, len(nums) + 1):
            prefix_sum = prefix_sum + nums[i-1]
            # this is sum from 0 to i - 1 
            index_to_prefix_sum[prefix_sum] = i - 1
            if prefix_sum - k in index_to_prefix_sum:
                # sum from 0 to previous_index(including)
                previous_index = index_to_prefix_sum[prefix_sum-k]
                current_length = i - 1 - previous_index
                print(current_length)
                result = min(result, current_length)
        
        return result if result != float('inf') else -1
        