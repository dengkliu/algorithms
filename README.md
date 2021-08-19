# Algorithms

## 1. Sorting (Easy)
* Quick sort
* Merge sort

## 2. Prefix Sum 前缀和
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**.

### 1） Definition
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/PrefixSum.java) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefixSum2Dimention.java)

### 2）Coding Problems
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/%5BEasy%5DMaximumSubarray.java)
* [Shortest Subarray Sum Equals to K II](https://github.com/dengkliu/algorithms/blob/master/%5BMedium%5DSubarraySumEqualK.java)
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/%5BHard%5DShortedSubarraySumAtLeastK.java)
* [Matrix Restoration](https://github.com/dengkliu/algorithms/blob/master/MatrixRestoration.java)
* [Product of Array Except Itself](https://github.com/dengkliu/algorithms/blob/master/ProductOfArrayExceptSelf.java)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java)

## 3. Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

### 1）Coding Problems
* [Number of Airplanes in the Sky](https://github.com/dengkliu/algorithms/blob/master/NumberOfAirplanesInTheSky.java)

## 4. Two Pointers (Medium) 双指针

## 5. Binary Search (Medium) 二分法

### Coding Problems
* [Maximum Number in Mountain Sequence](https://github.com/dengkliu/algorithms/blob/master/MaximumNumberInMountainSequence.java)
* [Find word](https://github.com/dengkliu/algorithms/blob/master/FindWords.java)
* [Search in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/SearchInRotatedSortedArray.java)
* [Wood Cut](https://github.com/dengkliu/algorithms/blob/master/WoodCut.java)

## 6. BFS (Easy) 宽度优先搜索
* [Template](https://github.com/dengkliu/algorithms/blob/master/BFS.java)
### 1）Get Topological Order
  * In-degree and Out-degree. Starting point has 0 in-degree. 
  * How to verify there exists topologifcal order - After BSF, whether the sequence length is equal to the total number of nodes
  * [Solution](https://www.jiuzhang.com/problem/topological-sorting/#tag-lang-java)
### 2）Get Shortest Path
   * Simple graph (no direction, no weights on each edge, same distance to nodes in next layer)
     * Kight Shortest Path II - https://www.lintcode.com/problem/630
     * Build Post Office II - https://www.lintcode.com/problem/573
     * Sliding Puzzle II - https://www.lintcode.com/problem/794
   * Complex graph - Shortest Path Faster Algorithm (SPFA) 
     * Modern Ludo I - https://www.lintcode.com/problem/1565
     * The Maze II - https://www.lintcode.com/problem/789
### 3）Connectivity
* **Longest Path on a Tree**
  * Longest path on a tree - https://www.lintcode.com/problem/1469

## 7. DFS (Hard) 深度优先搜索
* Divide and Conquer. 
  * What should be returned form next level?
  * What is the result at each level?
### 1）Coding Problems
* The diameter of binary tree - https://www.lintcode.com/problem/1181

## 8. Binary Tree Traversal (Easy)

## 9. Dynamic Programming (Hard) 动态规划

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection
of **simpler subproblems**, solving each of those subproblems **just once**, and **storing their solutions** 
using a memory-based data structure(array, map, etc). 

Trade the space complexity for time complexity.

### 1）Coordinate DP 坐标型型动态规划 (路径 + 方案总数)
* Related coding questions
  * Climbing Stairs
  * Rat Jump - https://www.lintcode.com/problem/1861/ 

### 2）Backpack DP 背包型动态规划
背包型问题一般会以前i个元素为状态。
  * Float Combination Sum https://www.lintcode.com/problem/1800/ （倒推法求套路）
  * Longest Common Subsequence - https://www.lintcode.com/problem/77/
  * Longest Increasing Subsequence

### 3）Interval DP 区间型动态规矩
  * Stone Game - https://www.lintcode.com/problem/476/

## 10. Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## 11. Useful data structures
### General Data Structures
* [Time Complexity Analysis](https://github.com/dengkliu/algorithms/blob/master/ds)
### Union Find
Union Find is used to solve connection problem, especially for dynamic data stream. BFS can only be used to solve connection problem for static data, for data stream, the time complexity will be horrible.

Union Find support O(1) time to merge two set which contains x and y - merge(x,y)
Union Find support O(1) time to query the set that contains x - find(x)
Union Find support O(1) time to query whether x and y are in the same set - isConnected(x,y)

The internal structure of Union Find is multiple multi-way trees. Each child node points to a father node. Each root corresponds to a set. We use a hashmap to map a child to a father. With this tree structure, we can do:
* Move upward to the rootn to find the set that contains an element - find(x)
* Check if two element belongs to the same set - have the same root - find(x) == find(y)
* Merget the set of x and set of y, set the parent of find(x) to find(y)

* Related coding questions
  * [Graph Validate Tree]()
### Trie
### Segment Tree
### Binary Indexed Tree
### Heap (Priority Queue)
### Skip List

## Tips
* First go through brute force approach
* Seek for optimal time complextiy you can achieve
  * If brute force is O(N), you should think about O(logn)
* StringBuilder is not thread safe, but StringBuffer is.
* Subarray is continuous, while subsquence is not. For an array with length N, there are N^2 subarrays and 2^N subsequences.
* Follow up questions
  * Constant -> Variable (2 sum -> k sum)
  * 1 dimentsion -> 2 dimension
  * == k -> >= k
  * shortest -> longest
  * postive -> negative
  * Immutable -> Mutable
  * Static input -> Data stream

## Other coding question
