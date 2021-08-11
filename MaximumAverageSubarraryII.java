// https://www.lintcode.com/problem/617/
// Given an array with positive and negative numbers, 
// find the maximum average subarray which length should be greater or equal to given length k.
// It's guaranteed that the size of the array is greater or equal to k.

// Input:
// [1,12,-5,-6,50,3]
// 3
// Output:
// 15.667

public class Solution {

    /**
     * @param nums: an array with positive and negative numbers
     * @param k: an integer
     * @return: the maximum average
     */
    public double maxAverage(int[] nums, int k) {
        // write your code here
        // [1, 12, -5, -6, 50, 3]
        // [0, 1, 13, 8, 2, 52, 55]
        int n = nums.length;

        int[] prefixSum = new int[n + 1];

        prefixSum[0] = 0;

        for (int i = 1; i < prefixSum.length; i ++) {
            prefixSum[i] = prefixSum[i-1] + nums[i-1];
        }
        
    }
}