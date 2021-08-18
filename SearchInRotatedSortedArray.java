// https://www.lintcode.com/problem/62/
// Suppose a sorted array is rotated at some pivot unknown to you beforehand.

// (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
// You are given a target value to search. If found in the array return its index, otherwise return -1.
// You may assume no duplicate exists in the array.

// Example
// array = [4, 5, 1, 2, 3]
// target = 1

// Brute force - O(N)
// Binary search - 因为旋转过，所以单调性被破坏了
// 这样可以找到那个最大的值，把两边分成两个单调区间，再进行binary search
public class Solution {
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    public int search(int[] A, int target) {

        int result = -1;

        if (A == null || A.length == 0) {
            return result;
        }

        // O(log(N))
        int index = findMaximumNumberIndex(A);

        // Tips : 把简单特殊的情况分出来放在前面
        if (target == A[0]) {
            return 0;
        } else if (target > A[0] || index == A.length - 1) { // 假如没有旋转过 一直是递增的 就在左边找
            result = binarySearch(target, A, index, false);
        } else if (target < A[0]) { // 小于第一个数 说明在右边 去右边找
            result = binarySearch(target, A, index, true); 
        } 

        return result;

    }

    int findMaximumNumberIndex(int[] A) {

        int start = 0;
        int end = A.length - 1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;

            if (A[mid] > A[0]) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return A[start] > A[end] ? start : end; 

    }

    int  binarySearch(int target, int[] A, int index, boolean searchInTheRight) {

        int start;
        int end;

        if (searchInTheRight) {
            start = index + 1;
            end = A.length - 1;
        } else {
            start = 0;
            end = index;
        }

        while (start + 1 < end) {
            int mid = start + (end - start)/2;

            if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] == target) {
            return start;
        }
        
        if (A[end] == target) {
            return end;
        }

        return -1;

    }
}