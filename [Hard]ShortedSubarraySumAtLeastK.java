// https://www.lintcode.com/problem/1507/

// Return the length of the shortest, non-empty, 
// contiguous subarray of A with sum at least K.

// 1 <= A.length <= 0000
// - 10 ^ 5 <= A[i] <= 10 ^ 5
// 1 <= k < 10^9

// [5, -1, 2, 3, 1] K = 8
// Output: 4 [5, -1, 2, 3]

// Brute Force - enumerate the start and end of the subarray, 
//    calculate the sum for each of them, and check if it >= K
//    for (int start = 0; start < n; start ++) {
//        for (int end = start + 1; end < n; end ++) {
//             for (int k = start; k < end; k ++) {
//             }
//        }
//    }
// 2. Calculate Prefix Sum beforehand. Don't need to calculate the sum of subarray again.
//    Still need to enumerate the start and end of the subarray. There are N^2 combinations
//    O(N^2)
// 3. What algorithms are faster than O(N^2)?
//    NlogN -> 60% n 次 LogN logN -> binary search, or heap
//             20% logN 次 N 次操作
