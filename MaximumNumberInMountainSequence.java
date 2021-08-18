// https://www.lintcode.com/problem/585

// Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).
// Arrays are strictly incremented, strictly decreasing

// Input: nums = [1, 2, 4, 8, 6, 3] 
// Output: 8

// Find the first num that the next number is smaller
// O(N) - scanning the array
// O(logN)Use binary search to narrow down
public class Solution {
    /**
     * @param nums: a mountain sequence which increase firstly and then decrease
     * @return: then mountain top
     */
    public int mountainSequence(int[] nums) {

        int start = 0;

        int end = nums.length - 1;

        while (start + 1 < end) {
            
            int mid = start + (end - start)/2;

            if (nums[mid] < nums[mid + 1]) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return nums[start] < nums[end] ? nums[end] : nums[start];

    }
}