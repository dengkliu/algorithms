# https://www.lintcode.com/problem/41/
# Given an array of integers, find a contiguous subarray 
# which has the largest sum and return the sum
# nums = [−2,2,−3,4,−1,2,1,−5,3] output 6 = [4, -1, 2, 1]
# Time complexity: O(n)

# [-2, 2, -3, 4, -1, 2, 1, -5, 3]
# prefix Sum -        [0, -2, 0, -3, 1, 0, 2, 3, -2, 1]
# minmum prefix sum - [0, -2, -2, -3, -3, -3, -3, -3, -3]

# 1. Brute Force - iterate the start and end of the subarray, 
#    calculate the sum for each of them, and get the minimum.
#    O(N^3)
#    for (int start = 0; start < n; start ++) {
#        for (int end = start + 1; end < n; end ++) {
#             for (int k = start; k < end; k ++) {
#             }
#        }
#    }
# 2. Calculate Prefix Sum beforehand. Don't need to calculate the sum of subarray again.
#    Still need to enumerate the start and end of the subarray. There are N^2 combinations
#    O(N^2)
# 3. Let's think in this way. We just need to enumerate the end. 
#    We don't have length constraint and we don't know where the start can be, but we know for an end, the start must
#    be from 0 to end - 1. The start must be at the index which prefixSum[start] is the minimum among 0 to end, 
#    to make prefixSum[end + 1] - prefixSum[start] the maximum.  The minimim prefixSum[start] among 0 to end can 
#    be found while enumerate the end, and it is O(1) time to fetch it later
#    Enumerating the end can be done in O(N)

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {

    	// Edge case check
    	if (nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length;

        // prefix[i] - the sum of first i numbers in the array
        int[] prefixSum = new int[n+1];
        prefixSum[0] = 0; 

        // Tracking the minimum prefix sum so far. Initialized as 0 (the first 0 number sum)
        int minPrefixSum = 0;

        // 准备好打擂台
        int result = Integer.MIN_VALUE;

        // Starting from adding 1 number
        for (int i = 1; i < n + 1; i ++) {
            prefixSum[i] = prefixSum[i-1] + nums[i-1];

            // Now get the maximum subarray ending in this number
            // by substracting the previous minimum prefix sum
            result = Math.max(result, prefixSum[i] - minPrefixSum);
            
            // Updating the minimum prefix sum
            minPrefixSum = Math.min(minPrefixSum, prefixSum[i]);
        }

        return result;

    }
}

