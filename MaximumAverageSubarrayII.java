// https://www.lintcode.com/problem/617
// Given an array with positive and negative numbers, 
// find the maximum average subarray which length should be greater or equal to given length k.

// It's guaranteed that the size of the array is greater or equal to k.

// Input:
// [1,12,-5,-6,50,3]
// 3
// Output:
// 15.667
// Explanation:
// (-6 + 50 + 3) / 3 = 15.667

// 1. Brute-Force
//    Enumerate the start and end of the subarray and calculate the sum and average for the subarray.
//    Then compare. O(N^3)
// 2. Build prefixSum array, which can help look up subarray sum in O(1) time
//    but we still need to enumerate the start and end, which is O(N^2) time
// 3. Ask the interviewer what can be the best time complexity
//    What could be better than O(N^2) is O(NlogN)
//    NlogN -> number of logN operations, each one take O(N) time
//    What is the solution set of this problem? 
//    The maximum average must be between the minimum and maximum element in this array!!
//    Therefore the problem reduced to 
//    Can you find a subarray of size >= k, that the avarage of the subarray is equal or greater than this avg?

//    Okay now we can enumerate the end again.
//    For subarrays ending in this element, it needs to be longer than k, this is an upper bound
//    It is great because we don't have to maintain a window and remove elements and keep tracking the minimum with heap
//    We can find the minimum left sum in O(1) time and just update it when the end moves.
//    We look for minimum left sum because we want to maximize the subarray sum, and compare with the lower bound avg.
//    If the maximum cannot reach the lower bound, this end doens't work. 

//    There is a great trick here, we hate calcuating the length of subarray and do division
//    We substract the avg from each element.
//    So the problem reduced to 
//    Can you find a subarray of size >= k, that the avarage of the subarray is equal or greater than 0?

public class Solution {

    /**
     * @param nums: an array with positive and negative numbers
     * @param k: an integer
     * @return: the maximum average
     */
    public double maxAverage(int[] nums, int k) {
        // write your code here
        double minValue = Integer.MAX_VALUE;
        double maxValue = Integer.MIN_VALUE;
        double mid;

        for (int i = 0; i < nums.length; i ++) {
            minValue = Math.min(nums[i], minValue);
            maxValue = Math.max(nums[i], maxValue);
        }

        while (minValue + 1e-5 < maxValue) {

            mid = minValue + (maxValue - minValue)/2;

            if (canFind(mid, nums, k)) {
                minValue = mid;
            } else {
                maxValue = mid;
            }
        }

        return minValue;
    }

    // for a given avg, can you find a subarray of size >= k, that the avarage of the 
    // subarray is greater than avg
    boolean canFind(double avg, int[] nums, int k) {

        // We substract avg from each element
        // The problem reduced to 
        // For a given avg, can you find a subarray of size >= k, that sum of the subarray 
        // is greater or equal to 0
        double[] nums2 = new double[nums.length];
        for (int i = 0; i < nums.length; i ++) {
            nums2[i] = nums[i] - avg;
        }

        double[] prefixSum = new double[nums2.length + 1];
        prefixSum[0] = 0;

        for (int i = 1; i < prefixSum.length; i ++) {
            prefixSum[i] = prefixSum[i-1] + nums2[i-1];
        }
        
        // [1, 2, 3, 4]
        // [0, 1, 3, 6, 10] 
        // [0, 1, 2, 3, 4]
        // k = 3
        double leftSumMinimum = 0;

        // Here the length must be greater than K
        // Therefore the ends start from k, then we start including more numbers
        int end = k;
        for (; end < prefixSum.length; end ++) {
            if (prefixSum[end] - leftSumMinimum >=0) {
                return true;
            }
            leftSumMinimum = Math.min(leftSumMinimum, prefixSum[end - k + 1]);
        }

        // What if we look for length <= k?
        // We can use heap, add all elements from 0 to K, and find minimum, 
        // and keep removing elements out of range

        return false;
    }
}