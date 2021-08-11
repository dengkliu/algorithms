// Given an array of n integers where n > 1, nums, 
// return an array output such that output[i] is equal to the product of 
// all the elements of nums except nums[i].

// Input: [1,2,3,4]
// Output: [24,12,8,6]

// Brute force: O(N^2)
// Use prefix product
// For each index, the result is prefixProductLeftToRight[i-1]*prefixProductRightToLeft[i+1]
// Time complexity O(N)
// Space complexity O(N)
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: the product of all the elements of nums except nums[i].
     */
    public int[] productExceptSelf(int[] nums) {

    	// [1, 2, 3, 4]
        int n = nums.length;

        // we can build this in place
        int[] result = new int[n];

        int left = 1;
        for (int i = 0; i < n; i ++) {
            left = left * nums[i];
            result[i] = left;
        }
        // result = [1, 2, 6, 24]

        // right = 1
        // result = [1, 2, 6, 6] 6 * 1
        // right = 4
        // result = [1, 2, 8, 6] 2 * 4
        // right = 12 
        // result = [1, 12, 8, 6] 1 * 12
        // right = 24
        // result = [24, 12, 8, 6] 1 * 24
        int right = 1;
        for (int i = n - 1; i >=0; i --) {
            result[i] = (i == 0 ? 1 : result[i-1]) * right;
            right = right * nums[i];
        }

        return result;
    }
}