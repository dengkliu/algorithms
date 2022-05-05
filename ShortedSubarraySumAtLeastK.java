// https://www.lintcode.com/problem/1507/

// Return the length of the shortest, non-empty, 
// contiguous subarray of A with sum at least K.

// 1 <= A.length <= 10000
// - 10 ^ 5 <= A[i] <= 10 ^ 5
// 1 <= k < 10^9

// [5, -1, 2, 3, 1] K = 8
// Output: 4 [5, -1, 2, 3]

// 1. Brute Force - enumerate the start and end of the subarray, 
//    calculate the sum for each of them, and check if it >= K
//    O(N^3)
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
//    要么是 O(NlogN) 要么是 O(N)
//    O(NlogN) --- 二分法
//    二分法要求左右两边不一样 怎么寻找不一样呢？在什么上面二分呢？
//    假如一个数组，不存在任何一个子数组和大于或者等于看K，那么它的所有子数组，也不会存在。
//    对于一个数组，check是否存在子数组大于等于K，可以在O(N)时间完成 --> 用heap存储prefix sum的min，来得到最大的子数组和，与K作比较。
//    所以可以在数组的长度上二分，我们知道最后的解一定在0到A.length之间


// Binary search on the solution set
//                       find the shortest subarrary with SUM >= 4
// array elements           4     | -2   |  3    |  -4  |  5   | -6   |
// subarray length          0     |  1   |  2    |  3   |  4   |  5   | 6
// sum>= 4 and length == x  false | true | false | false| false| true | false
// sum>= 4 and length <= x  false | true | true  | true | true | true | true

// for binary search, we are looking for OOO|XXX pattern 
// so we know whether to choose right or left
// so we want to do binary search on (sum>=K and length <= x)
// To do this: We want to scan the entire array for a specific shortest length - 
//     I. We enumerate the end 
//     II. Because we have length constraint, we have to maintain a set of numbers within the length range, so we not only need to add, but also remove. 
//     Besides, we are looking for a sum at least K, so we can compare the maximum sum with the K, 
//     if the maximum sum is still less than K, we don't need to enumerate other positions, we can just skip to speed up. 
//     So we need a data sturcture that can add and remove and give us the minimum, that is Heap.
//     III. Whether we find a subarray that meet the requirements, we look for less shortest length.
//     Until the binary search ends, which means either start and end is next to each other. 
//     So the solution can be either the start or end. We check the enitire 
//     The overall time complexity is NlogN.


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


// 4. Can we do at O(N) time?

// Can we use two pointers here? Why?

// We can not use two pointers because there might be negative number, 
// so we don't know which direction to move for the left pointer, should we move left to include more number 
// or should we move right to include less?

// We can use monotonic queue. We can keep prefixSum in an increasing order. 
// 为什么？因为这样的话栈尾的prefixSum就是最小的，我们要找的就是之前的最小值，
// 这样才能得到最大的区间sum, 假如这个sum都没有K大的话，说明以当前end，找不到解。
// 这样只能看下一个end。反之，就可以试试缩小范围。

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

        int[] prefixSum = getPrefixSum(A);

        Deque<Integer> deque = new ArrayDeque<>();

        deque.add(0);

        int result = Integer.MAX_VALUE;

        for (int i = 1; i < prefixSum.length; i++) {

            while(!deque.isEmpty() 
                    && prefixSum[deque.peekLast()] >= prefixSum[i]) {
                deque.pollLast();
            }

            while (!deque.isEmpty() && 
                    prefixSum[i] - prefixSum[deque.peekFirst()] >= K) {
                result = Math.min(result, i - deque.peekFirst());
                deque.pollFirst();
            }

            deque.add(i);
        }

        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private int[] getPrefixSum(int[] A) {
        int[] prefixSum = new int[A.length + 1];

        prefixSum[0] = 0;

        for (int i = 1; i < A.length + 1; i ++) {
            prefixSum[i] = prefixSum[i-1] + A[i-1];
        }

        return prefixSum;
    }
}








