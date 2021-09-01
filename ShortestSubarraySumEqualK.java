
// https://www.lintcode.com/problem/1844/
// Given an array of integers and an integer k, 
// you need to find the minimum size of continuous no-empty subarrays whose sum equals to k, and return its length.
// if there are no such subarray, return -1.

// Input: nums = [1,1,1,2] and k = 3
// Output: 2 = 1 + 2

// 1. Brute Force - enumerate the start and end of the subarray, 
//    calculate the sum for each of them, and check if it is K。 It is going to be O(N^3)
//    for (int start = 0; start < n; start ++) {
//        for (int end = start + 1; end < n; end ++) {
//             for (int k = start; k < end; k ++) {
//             }
//        }
//    }
// 2. Calculate Prefix Sum beforehand. Don't need to calculate the sum of subarray again.
//    Still need to enumerate the start and end of the subarray. There are N^2 combinations
//    O(N^2)
// 3. Let's think in this way. We just need to enumerate the end. The start must be at the index
//    which make sure that prefixSum[end] - prefixSum[start -1] is the K. We don't have length constraints here, so the start 
//    can be from 0 to end - 1. We can keep tracking the subarray length.
//    How do we find prefixSum[start-1] in O(1) time? We can use hashmap. Hashmap checks key existance in O(1) time
//    So we can have a hashmap with sum to index pair. 
//    We enumerate the end from index 0 to n-1, for each one we look up the hashmap. 
//    This can be done in O(N)

public class Solution {
    
    /*
     * @param nums: a list of integer
     * @param k: an integer
     * @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
     */

    // [1, 1, 1]
    // [-1 -> 0, ]

    public int subarraySumEqualsKII(int[] nums, int k) {

        if (nums == null || nums.length == 0) {
            return -1;
        }

        int n = nums.length;
        
        // 这里我们选择优化 因为我们有hashmap存放prefix sum
        // 我们可以不用数组了
        long prefixSum = 0;

        // This should be sum to index
        Map<Long, Integer> sumToIndexMap = new HashMap<>();

        // 默认为初始Index为-1
        sumToIndex.put((long)0, -1);

        // 准备打擂台
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length; i ++) {
            
            prefixSum = prefixSum + nums[i];

            if(sumToIndexMap.containsKey(prefixSum - k)) {
                // We find A[0] + .. + A[start] is prefixSum[i] - K
                // Therefore A[start + 1] + ... A[i -1] is K
                int start = sumToIndex.get(prefixSum - k);
                result = Math.min(result, i - start);
            }

            sumToIndex.put(prefixSum, i);
        }

        return result == Integer.MAX_VALUE ? -1 : result;
    }
}
