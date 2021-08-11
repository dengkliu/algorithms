// https://www.lintcode.com/problem/1507/

// Return the length of the shortest, non-empty, 
// contiguous subarray of A with sum at least K.

// 1 <= A.length <= 0000
// - 10 ^ 5 <= A[i] <= 10 ^ 5
// 1 <= k < 10^9

// [5, -1, 2, 3, 1] K = 8
// Output: 4 [5, -1, 2, 3]

// 1. Brute Force - enumerate the start and end of the subarray, 
//    calculate the sum for each of them, and check if it >= K
//    for (int start = 0; start < n; start ++) {
//        for (int end = start + 1; end < n; end ++) {
//             for (int k = start; k < end; k ++) {
//             }
//        }
//    }
// 2. Calculate Prefix Sum beforehand. Don't need to calculate the sum of subarray again.
//    Still need to enumerate the start and end of the subarray, as we actually don't know 
//    for each end, where the start could be, and what could be the shortest length.
//     There are N^2 combinations
//    O(N^2). 
// 3. What algorithms are faster than O(N^2)?
//    NlogN -> 60% n 次 LogN operation logN -> binary search, or heap, segment tree
//             20% logN 次 N 次操作 use O(N) time to check the answer

//    Hint: can we enumerate the shortest length here?
//    The solutuon to this problem definitely has an range, from length 1 to N (or -1 if not found)
//    Can we do a binary search on the solution set?


// Binary search on the solution set
//                       find the shortest subarrary with SUM >= 4
// array elements           4     | -2   |  3    |  -4  |  5   | -6   |
// subarray length          0     |  1   |  2    |  3   |  4   |  5   | 6
// sum>= 4 and length == x  false | true | false | false| false| true | false
// sum>= 4 and length <= x  false | true | true  | true | true | true | true

// for binary search, we are looking for OOO|XXX pattern 
// so we know whether to choose right or left
// so we want to do binary searhc on (sum>=K and length <= x)
// To do this: We want to scan the entire array for a specific shortest length - 
// 1. We enumerate the end 2. We keep a window of size k, and enumerate the start in the window.
// For enumerating the start, we can actually start from the minimum prefixSum, if we substract the minimum
// prefixSum and it is still less than K, we don't need to enumerate other positions, we can just skip to speed up.
// Heap can be used to find minimum/maximum and keep order.
// Whether we find a subarray that meet the requirements, we look for less shortest length.
// Until the binary search ends, which means either start and end is next to each other. 
// So the solution can be either the start or end. We check the enitire 
// The overall time complexity is NlogN.

class IndexValuePair {
    int index;
    int value;

    int getIndex() {
        return index;
    }
    
    int getValue() {
        return value;
    }

    IndexValuePair(int index, int value){
        this.index = index;
        this.value = value;
    }
}

// Java heap 删除 node 的 time complexity is O(N) -> O(N) time to find the element, and O(logN) time to delete it
class Heap {

    private Queue<IndexValuePair> minheap;

    private Set<Integer> deleteSet;

    public Heap() {
        minheap = new PriorityQueue<>((p1, p2) -> (p1.getValue() - p2.getValue()));
        deleteSet = new HashSet<>();
    }

    public void push(int index, int value) {
        minheap.add(new IndexValuePair(index, value));
    }

    // delete when you pop and peek.
    private void lazyDeletion() {

        while(minheap.size()!= 0 && deleteSet.contains(minheap.peek().getIndex())) {

        	IndexValuePair pair = minheap.poll();

            deleteSet.remove(pair.getIndex());
        }
    }

    public IndexValuePair top() {
        lazyDeletion();
        return minheap.peek();
    }

    public void pop() {
        lazyDeletion();
        minheap.poll();
    }

    // delete O(1)
    public void delete(int index) {
        deleteSet.add(index);
    }

    public boolean isEmpty() {
        return minheap.isEmpty();
    }

}

public class Solution {
    /**
     * @param A: the array
     * @param K: sum
     * @return: the length
     */
    public int shortestSubarray(int[] A, int K) {

        if (A == null || A.length == 0) {
            return -1;
        }

        int n = A.length;
        int[] prefixSum = new int[n + 1];

        prefixSum[0] = 0;

        for (int i = 1; i < n + 1; i ++) {
            prefixSum[i] = prefixSum[i-1] + A[i-1];
        }

        // Binary search on the solution set
        int start = 1, end = A.length;
        while(start + 1 < end) {
            
            int mid = start + (end - start)/2;

            if (isValid(mid, K, prefixSum)) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (isValid(start, K, prefixSum)) {
            return start;
        }

        if (isValid(end, K, prefixSum)) {
            return end;
        }

        return -1;
    }

    boolean isValid(int length, int K, int[] prefixSum) {

        Heap minheap = new Heap();

        for (int end = 0; end < prefixSum.length; end ++) {
            int index = end - length - 1;
            // index可能会为负数 但是根本不用管 因为不可能在heap中存在了
            // heap里的deleteSet会自动check
            minheap.delete(index);

            // 只要找到一个就可，没有就继续，因为以这个点为终点的subarray不可能又更大的sum了
            if(!minheap.isEmpty() && prefixSum[end] - minheap.top().getValue() >= K) {
                return true;
            }

            minheap.push(end, prefixSum[end]);
        }

        return false;
    }
}







