// https://www.lintcode.com/problem/617/
// Given an array with positive and negative numbers, 
// find the maximum average subarray which length should be greater or equal to given length k.
// It's guaranteed that the size of the array is greater or equal to k.

// Input:
// [1,12,-5,-6,50,3]
// 3
// Output:
// 15.667

// 1. Brute Force
//    Enumerate the start and end, and calcuate the sum. O(N^3)
// 2. With prefixSum array. O(N^2)
// 3. What time complexity can be better O(N^2)? 
//    O(NlogN)
//    logN 次 O(N) 操作
//    Binary search
//    解空间？the maximum average must be between the maximum and minimum number
//    所以对于每个avg, 题目变成 - 是否存在一个长度大于等于k的数组，average大于avg?
//    加入存在，avg可以继续放大，不然就减小。
//    怎么验证是否存在一个长度大于等于k的数组，average大于等于avg?
//    这里为了排除掉length对于average的影响，我们可以把avg从每个元素减去
//    题目变成 怎么验证是否存在一个长度大于等于k的数组，sum大于0
//    那么这里我们又回到了 寻找一个给定end的subarray的sum最大值 假如最大值都小于0 那就skip
//    这里是有长度限制的，长度要大，所以不用减元素，而是要往右加元素。prefixsum的最小值
//    只需要跟新加入的元素比较，所以不需要data structure来hold.

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