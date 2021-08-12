# Algorithms

## String Processing (Easy)

## Sorting (Easy)
* Quick sort
* Merge sort

## Prefix Sum 前缀和
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**.

### Definition
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/PrefixSum.java) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefixSum2Dimention.java)

### Coding Problems
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/%5BEasy%5DMaximumSubarray.java)
* [Shortest Subarray Sum Equals to K II](https://github.com/dengkliu/algorithms/blob/master/%5BMedium%5DSubarraySumEqualK.java)
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/%5BHard%5DShortedSubarraySumAtLeastK.java)
* [Matrix Restoration](https://github.com/dengkliu/algorithms/blob/master/MatrixRestoration.java)
* [Product of Array Except Itself](https://github.com/dengkliu/algorithms/blob/master/ProductOfArrayExceptSelf.java)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java)
* Find words - https://www.lintcode.com/problem/194/

## Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

### Coding Problems
*  Number of Airplanes in the Sky

## Two Pointers (Medium) 双指针

## Binary Search (Medium) 二分法

### Coding Problems
* Maximum Number in Mountain Sequence - https://www.lintcode.com/problem/585

## BFS (Easy) 宽度优先搜索
* [Template](https://github.com/dengkliu/algorithms/blob/master/BFS.java)
* **Get Topological Order**
  * In-degree and Out-degree. Starting point has 0 in-degree. 
  * How to verify there exists topologifcal order - After BSF, whether the sequence length is equal to the total number of nodes
  * [Solution](https://www.jiuzhang.com/problem/topological-sorting/#tag-lang-java)
*  **Get Shortest Path**
   * Simple graph (no direction, no weights on each edge, same distance to nodes in next layer)
     * Kight Shortest Path II - https://www.lintcode.com/problem/630
     * Build Post Office II - https://www.lintcode.com/problem/573
     * Sliding Puzzle II - https://www.lintcode.com/problem/794
   * Complex graph - Shortest Path Faster Algorithm (SPFA) 
     * Modern Ludo I - https://www.lintcode.com/problem/1565
     * The Maze II - https://www.lintcode.com/problem/789
* **Connectivity**
* **Longest Path on a Tree**
  * Longest path on a tree - https://www.lintcode.com/problem/1469

## DFS (Hard) 深度优先搜索
* Divide and Conquer. 
  * What should be returned form next level?
  * What is the result at each level?
### Coding Problems
* The diameter of binary tree - https://www.lintcode.com/problem/1181

## Binary Tree Traversal (Easy)

## Dynamic Programming (Hard) 动态规划
* Related coding questions
  * Longest Common Subsequence - https://www.lintcode.com/problem/77/
  * Longest Increasing Subsequence 

## Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## Useful data structures
### General Data Structures
* [Time Complexity Analysis](https://github.com/dengkliu/algorithms/blob/master/ds)
### Union Find
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
