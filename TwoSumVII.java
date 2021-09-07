// https://www.lintcode.com/problem/1879/

// Given an array of integers that is already sorted in ascending absolute order, find two numbers so that the sum of them equals a specific number.

// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Note: the subscript of the array starts with 0

// You are not allowed to sort this array.

// It is guaranteed that all numbers in the numsnums is distinct.

// The length of numsnums is <= 100000.

// The number in nums is <= 10^9

// Input: [0,-1,2,-3,4] 1
// Output: [[1,2],[3,4]]

// 1. Brute force - break the array down to two parts - postive and negative and then do regular 2 sum. O(N) space.

// 2. Can we do O(1) space?

//    1) for negaive, how to find the next bigger num, as it can be postive?
//    2) for postive, how to find the next smaller num, as it can be negative?

// If we use 2 pointers here still, where are the start and end?
// What is the termination condition

public class Solution {
    /**
     * @param nums: the input array
     * @param target: the target number
     * @return: return the target pair
     */
    public List<List<Integer>> twoSumVII(int[] nums, int target) {

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        int minNumIndex = 0, maxNumIndex = 0;
        int minNum = Integer.MAX_VALUE, maxNum = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] < minNum) {
                minNum = nums[i];
                minNumIndex = i;
            }

            if (nums[i] > maxNum) {
                maxNum = nums[i];
                maxNumIndex = i;
            }
        }

        int start = minNumIndex;
        int end = maxNumIndex;

        while (nums[start] < nums[end]) {

            int curr = nums[start] + nums[end];

            if (curr < target) {
                start = findNextBiggerStart(start, nums);
                if (start == -1) {
                    break;
                }
            } else if (curr > target) {
                end = findNextSmallerEnd(end, nums);
                if (end == -1) {
                    break;
                }
            } else {
                List<Integer> indexes = new ArrayList<>();
                indexes.add(Math.min(start, end));
                indexes.add(Math.max(start, end));
                result.add(indexes);

                end = findNextSmallerEnd(end, nums);
                start = findNextBiggerStart(start, nums);
                if (end == -1 || start == -1) {
                    break;
                }
            }
        }

        return result;
    }

    // Find the next bigger value
    int findNextBiggerStart(int index, int[] nums) {
        
        if (nums[index] < 0) {
            // 找那个更大一些的负数
            for (int i = index - 1; i >= 0; i --) {
                if (nums[i] < 0) {
                    return i;
                }
            }

            // 假如都没有找到负数，就得找最小的那个正数
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] >= 0) {
                    return i;
                }
            }

            return -1;
        }

        // 正数的话，直接找下一个更大的正数
        for (int i = index + 1; i < nums.length; i ++) {
            if (nums[i] >= 0) {
                return i;
            }
        }
        
        return -1;   
    }

    // 找一个更小的数
    int findNextSmallerEnd(int index, int[] nums) {

        // 如果从正数开始找 就有可能找到负数
        if (nums[index] > 0) {
            
            // 如果找不到更小的正数了
            for (int i = index - 1; i >= 0; i --) {
                if (nums[i] > 0) {
                    return i;
                }
            }

            for (int i = 0; i < nums.length; i ++) {
                if (nums[i] <= 0) {
                    return i;
                }
            }
        }
        
        // 从负数开始找 只有可能往后找
        for (int i = index + 1; i < nums.length; i ++) {
            if (nums[i] <= 0) {
                return i;
            }
        }

        return -1;
    }
}

