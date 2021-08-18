// https://www.lintcode.com/problem/183/
// Given n pieces of wood with length L[i] (integer array). 
// Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
// What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

// Input [232, 124, 456]
// K = 7
// Output: 114

// We don't know what would the maximum length can be
// but we know the boundary
// it at least should be 1
// and at most as much as the max number in the array
// So we can do binary search in the solution space
public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    public int woodCut(int[] L, int k) {
        
        // write your code here
        if (L == null || L.length == 0) {
            return 0;
        }

        // 解空间！！是可以取到最大值得，越大越好，不一定
        // 要分解每个数，只要有超过K个数字就行
        int end = Integer.MIN_VALUE;
        for (int i = 0; i < L.length; i ++) {
            end = Math.max(L[i], end);
        }

        int start = 1;

        while(start + 1 < end) {

            int mid = start + (end - start)/2;

            System.out.println( "Start " + start + " End " + end + " Mid " + mid);

            if (canFind(mid, L, k)) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (canFind(end, L, k)) {
            return end;
        }

        if (canFind(start, L, k)) {
            return start;
        }

        return 0;
    }

    boolean canFind(int target, int[] L, int k) {

        for (int i = 0; i < L.length; i++) {

            k -= L[i]/target;

            if (k <= 0) {
                return true;
            }
        }

        return false;
    }
}