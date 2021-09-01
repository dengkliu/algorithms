// https://www.lintcode.com/problem/838/
// Subarray Sum Equals K
// Given an array of integers and an integer k, 
// you need to find the total number of continuous subarrays whose sum equals to k.

// Input: nums = [1,1,1] and k = 2
// Output: 2
// Explanation:
// subarray [0,1] and [1,2]

// Brute force - enumerate O(N^3)
// Use prefixSum and enumerate the end, use hashmap to store sum to index pair
// One sum can map to multiple indexes


public class Solution {
    /**
     * @param nums: a list of integer
     * @param k: an integer
     * @return: return an integer, denote the number of continuous subarrays whose sum equals to k
     */
    public int subarraySumEqualsK(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length;

        // prefixSum[i] = A[0] + ... + A[i-1];
        int[] prefixSum = new int[n+1];

        // This should be sum to index
        Map<Integer, Set<Integer>> sumToIndex = new HashMap<>();

        prefixSum[0] = 0;
        // 默认为初始Index为-1
        Set<Integer> indexSet = new HashSet<>();
        indexSet.add(-1);
        sumToIndex.put(0, indexSet);

        int result = 0;

        for (int i = 1; i < n + 1; i ++) {

            // now the end is i - 1 A[0] + ... + A[i-1]
            prefixSum[i] = prefixSum[i-1] + nums[i-1];

            Set<Integer> set = sumToIndex.containsKey(prefixSum[i]) ? 
            sumToIndex.get(prefixSum[i]) : new HashSet<>();

            set.add(i - 1);

            if(sumToIndex.containsKey(prefixSum[i] - k)) {
                result = result + sumToIndex.get(prefixSum[i] - k).size();
            }

            sumToIndex.put(prefixSum[i], set);
        }

        return result;
    }
}