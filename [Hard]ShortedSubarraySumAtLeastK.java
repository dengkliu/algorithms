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
//    NlogN -> 60% n 次 LogN operation logN -> binary search, or heap, segment tree
//             20% logN 次 N 次操作 use O(N) time to check the answer
//    The solutuon to this problem definitely has an range, from length 1 to N (or -1 if not found)


// Binary search on the solution set
//                       find the shortest subarrary with SUM >= 4
// array elements           4     | -2   |  3    |  -4  |  5   | -6   |
// subarray length          0     |  1   |  2    |  3   |  4   |  5   | 6
// sum>= 4 and length == x  false | true | false | false| false| true | false
// sum>= 4 and length <= x  false | true | true  | true | true | true | true

// for binary search, we are looking for OOO|XXX pattern 
// so we know whether to choose right or left
// so we want to do sum>=K and length <= x
//

