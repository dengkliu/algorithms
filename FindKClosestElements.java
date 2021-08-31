// Given target, a non-negative integer k and an integer array A sorted in ascending order, 
// find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
// Otherwise, sorted in ascending order by number if the difference is same.

// The value k is a non-negative integer and will always be smaller than the length of the sorted array.
// Length of the given array is positive and will not exceed 10^4
// Absolute value of elements in the array will not exceed 10^4

// Input: A = [1, 2, 3], target = 2, k = 3
// Output: [2, 1, 3]

// Brute and force: 计算每个数字和target的difference
// 然后跟据difference排序，可以用heap 但是复杂度度是 N*logN + K

// 可以用二分法 因为数组是sorted 可以找到离target最近的数
// 然后用two pointer向两边找次近的数
// 复杂度是 logN + K

public class Solution {
    /**
     * @param A: an integer array
     * @param target: An integer
     * @param k: An integer
     * @return: an integer array
     */
    public int[] kClosestNumbers(int[] A, int target, int k) {

        if (A == null || A.length == 0) {
            return null;
        }

        int[] result = new int[k];
        
        int start = 0;
        int end = A.length;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;

            if (A[mid] > target) {
                end = mid;
            } else {
                start = mid;
            }
        }

        int index = 0;

        while (start >= 0 && end < A.length && index < k) {

            int leftDistance = target - A[start];
            int rightDistance = A[end] - target;

            if (leftDistance <= rightDistance) {
                result[index] = A[start];
                start --;
                index ++;
            } else {
                result[index] = A[end];
                end ++;
                index ++;
            }
        } 

        while (index < k && start >= 0) {
            result[index] = A[start];
            start --;
            index ++;
        } 

        while (index < k && end < A.length) {
            result[index] = A[end];
            end ++;
            index ++;
        }

        return result; 

    }
}