# https://leetcode.com/problems/subarray-product-less-than-k/description/

# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        if k <= 1:
            return 0

        n = len(nums)
        prefix_product = 1
        result = 0
        
        end = 0
        for start in range(n):
            while end < n and prefix_product < k:
                prefix_product = prefix_product * nums[end]
                end += 1
                
            if prefix_product < k:
                result += end - start
            else:
                result += end - start - 1
            
            prefix_product = prefix_product / nums[start]
            
        return result

        # [10, 5, 2, 6]
        # start 0 end 0 --- product 1 
        # start 0 end 1 ---- product 10
        # start 0 end 2 ---- product 50
        # start 0 end 3 ---- product 100 result 3 - 0 - 1 = 2
        # start 1 end 3 ---- product 10  
        # start 1 end 4 ---- product 60 result 2 + 4 - 1 = 5
        # start 2 end 4 ---- product 12 result 5 + 4 - 2 = 7
        # start 3 end 4 ---- product 6  result 7 + 4 - 2 = 8