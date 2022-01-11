# https://www.lintcode.com/problem/838/
# Subarray Sum Equals K
# Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays whose sum equals to k.

# Input: nums = [1,1,1] and k = 2
# Output: 2
# Explanation:
# subarray [0,1] and [1,2]

# Brute force - enumerate O(N^3)
# Use prefixSum and enumerate the end, use hashmap to store sum to index pair
# One sum can map to multiple indexes

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):

        if not nums:
            return 0
        
        # write your code here
        sum_to_indexes={}
        sum_to_indexes[0] = [-1]

        prefix_sum = 0

        result = 0

        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i]
            if prefix_sum in sum_to_indexes:
                sum_to_indexes[prefix_sum].append(i)
            else:
                sum_to_indexes[prefix_sum] = [i]
            
            if prefix_sum - k in sum_to_indexes:
                result += len(sum_to_indexes[prefix_sum - k])
        
        return result