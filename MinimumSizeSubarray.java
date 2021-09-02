// Given an array of n positive integers and a positive integer s, 
// find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

// Input: [2,3,1,2,4,3], s = 7
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.

// 因为都是正整数
// 向右多加一个数 和一定增加
// 向左多减一个数 和一定减少
// 用同向的两个指针 来追踪所有以start为开头的满足条件的最小array
// O(N)
public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: An integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {

        int end = 0;
        int subArraySum = 0;
        int n = nums.length;
        int minimumSize = Integer.MAX_VALUE;

        for (int start = 0; start < n; start++) {
            while (end < n && subArraySum < s) {
                subArraySum += nums[end];
                end ++;
            }

            if (subArraySum >= s) {
                minimumSize = Math.min(minimumSize, end - start);
            }

            subArraySum -= nums[start];
        }

        return minimumSize == Integer.MAX_VALUE ? -1 : minimumSize;
    }
}