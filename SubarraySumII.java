// Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.

// Input: A = [1, 2, 3, 4], start = 1, end = 3
// Output: 4
// Explanation: All possible subarrays: [1](sum = 1), [1, 2](sum = 3), [2](sum = 2), [3](sum = 3).

// Prefix sum
// Two pointers.
public class Solution {
    /**
     * @param A: An integer array
     * @param start: An integer
     * @param end: An integer
     * @return: the number of possible answer
     */
    public int subarraySumII(int[] A, int start, int end) {

        if (A == null || A.length == 0) {
            return 0;
        }

        int[] prefixSum = new int[A.length + 1];

        for (int i = 1; i < A.length + 1; i ++) {
            prefixSum[i] = prefixSum[i-1] + A[i-1];
        }

        int left = 0, right = 0, result = 0;

        // Enumerate the end
        for (int i = 1; i < A.length + 1; i ++) {

            while(left < i && prefixSum[i] - prefixSum[left] > end) {
                left++;
            }

            while(right < i && prefixSum[i] - prefixSum[right] >= start) {
                right++;
            }

            result += right - left;
        }

        return result;
    }
}