# Algorithms

## String Processing (Easy)

## Sorting (Easy)
* Quick sort
* Merge sort

## Prefix Sum
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**.

### Definition
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/PrefixSum.java) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefixSum2Dimention.java)

### Coding Problems
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/MaximumSubarray.java)
* [Shortest Subarray Sum Equals to K II](https://github.com/dengkliu/algorithms/blob/master/SubarraySumEqualK.java)
* Shortest Subarray Sum At Least K - https://www.lintcode.com/problem/1507/
* Find words - https://www.lintcode.com/problem/194/

## Two Pointers (Medium)

## Binary Search (Medium)

### Coding Problems
* Maximum Number in Mountain Sequence - https://www.lintcode.com/problem/585

## Divide & Conquer (Easy)

## BFS (Easy)
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

## DFS (Hard)
* Divide and Conquer. 
  * What should be returned form next level?
  * What is the result at each level?
### Coding Problems
* The diameter of binary tree - https://www.lintcode.com/problem/1181

## Binary Tree Traversal (Easy)

## Dynamic Programming (Hard)
* Related coding questions
  * Longest Common Subsequence - https://www.lintcode.com/problem/77/
  * Longest Increasing Subsequence 

## Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/

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
  * == k => >= k
  * shortest -> longest
  * postive -> negative
