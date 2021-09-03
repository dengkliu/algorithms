# Algorithms

## 1. Sorting 排序
Both of them use divide and conquer.
* [Quick sort](https://github.com/dengkliu/algorithms/blob/master/QuickSort.java)
* [Merge sort](https://github.com/dengkliu/algorithms/blob/master/MergeSort.java)

## 2. Binary Tree Traversal 二叉树遍历

* [Inorder Traveral of Binary Tree - Iterative Version ](https://github.com/dengkliu/algorithms/blob/master/InoderTraversal.java)

## 3. Prefix Sum 前缀和
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**.

### Definition
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/PrefixSum.java) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefixSum2Dimention.java)

### Coding Problems
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/MaximumSubarray.java)
* [Subarray Sum Equals K](https://github.com/dengkliu/algorithms/blob/master/SubarraySumEqualK.java)
* [Shortest Subarray Sum Equals to K](https://github.com/dengkliu/algorithms/blob/master/ShortestSubarraySumEqualK.java)
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/ShortedSubarraySumAtLeastK.java)
* [Matrix Restoration](https://github.com/dengkliu/algorithms/blob/master/MatrixRestoration.java)
* [Product of Array Except Itself](https://github.com/dengkliu/algorithms/blob/master/ProductOfArrayExceptSelf.java)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java)

## 4. Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

### Coding Problems
* [Number of Airplanes in the Sky](https://github.com/dengkliu/algorithms/blob/master/NumberOfAirplanesInTheSky.java)

## 5. Two Pointers 双指针

Two pointers are usually used when:
* Sliding window problem
* Time complexity is O(N) (80%)
* In-place algorithm, you can not use extra space.
* Subarray or substring problem (50%)
* Palindrome problem (50%)

### [Same direction two pointers](https://github.com/dengkliu/algorithms/blob/master/SameDirectionTwoPointers.java)
Two pointers start from the head of array and go to the end.
* [Minimum Size Subarray Sum](https://github.com/dengkliu/algorithms/blob/master/MinimumSizeSubarray.java)
* [Substring With At Least K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/SubstringWithAtLeastKDistinctCharacters.java)
* [Minimum Window Substring](https://github.com/dengkliu/algorithms/blob/master/MinimumWindowSubstring.java)
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/Heaters.java)

### Fixed Size Sliding Window

* [Grumpy Bookstore Owner](https://github.com/dengkliu/algorithms/blob/master/GrumpyBookStoreOwner.java)

### Opposite direction two pointers
### Back direction two pointers

## 6. Binary Search 二分查询

You may want to use binary search when -
* The array is sorted
* When the interviewer ask you to find a solution that is better than O(N)
* Find a cut in the array, which makes the left half meet the condition, the other half don't.
* Find a maximum or minimum value to meet a certain requirement

### 1) Coding Problems
* [Maximum Number in Mountain Sequence](https://github.com/dengkliu/algorithms/blob/master/MaximumNumberInMountainSequence.java)
* [Find word](https://github.com/dengkliu/algorithms/blob/master/FindWords.java)
* [Search in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/SearchInRotatedSortedArray.java)
* [Wood Cut](https://github.com/dengkliu/algorithms/blob/master/WoodCut.java)
* [Copy Books](https://github.com/dengkliu/algorithms/blob/master/CopyBooks.java)
* [Find K Closet Elements](https://github.com/dengkliu/algorithms/blob/master/FindKClosestElements.java)
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/Heaters.java)

## 7. Breath-First Search 宽度优先搜索
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

## 8. Depth-First Search 深度优先搜索
* Divide and Conquer.
  * What should be returned form next level?
  * What is the result at each level?
### 1）Coding Problems
* The diameter of binary tree - https://www.lintcode.com/problem/1181

## 9. Dynamic Programming 动态规划

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection
of **simpler subproblems**, solving each of those subproblems **just once**, and **storing their solutions** 
using a memory-based data structure(array, map, etc). 

Trade the space complexity for time complexity.

### 1）Coordinate DP
* Climbing Stairs
* Rat Jump - https://www.lintcode.com/problem/1861/ 

### 2）Backpack DP 
* Float Combination Sum https://www.lintcode.com/problem/1800/
* Longest Common Subsequence - https://www.lintcode.com/problem/77/
* Longest Increasing Subsequence

### 3）Interval DP
* Related coding questions
* Stone Game - https://www.lintcode.com/problem/476/

### 4) Prefix DP
* Related coding questions
* [Longest Common Subsequence](https://github.com/dengkliu/algorithms/blob/master/LongestCommonSubsequence.java)

## 10. Monotonic Stack/Queue

### Coding problems
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/ShortedSubarraySumAtLeastK.java)

## 11. Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## 12. Useful data structures
### 1) Union Find
[Union Find](https://github.com/dengkliu/algorithms/blob/master/UnionFind.java) is used to solve connection problem, especially for dynamic data stream (online algorithm). BFS can only be used to solve connection problem for static data (therefore BFS is offline algorithm), for data stream, the time complexity will be horrible.

* Union Find support O(1) time to merge two set which contains x and y - merge(x,y)
* Union Find support O(1) time to query the set that contains x - find(x)
* Union Find support O(1) time to query whether x and y are in the same set - isConnected(x,y)

The internal structure of Union Find is multiple multi-way trees. Each child node points to a father node. Each root corresponds to a set. We use a hashmap to map a child to a father. With this tree structure, we can do:
* Move upward to the rootn to find the set that contains an element - find(x)
* Check if two element belongs to the same set - have the same root - find(x) == find(y)
* Merget the set of x and set of y, set the parent of find(x) to find(y)

Related coding questions
  * [Graph Validate Tree](https://github.com/dengkliu/algorithms/blob/master/GraphValidTreeII.java)
  * [Set Union](https://github.com/dengkliu/algorithms/blob/master/SetUnion.java)
  * [Account Merge](https://github.com/dengkliu/algorithms/blob/master/AccountMerge.java)
### 2) Trie

[Trie](https://github.com/dengkliu/algorithms/blob/master/Trie.java) is used to store strings while compressing the string common prefix. Its internal structure is a tree. The more common prefixes shared by the words in the dictionary, the more time saved. 

The best time complexity for insert word and find word is O(L).

Related coding questions
* [Add and Search Word - Data structure design](https://github.com/dengkliu/algorithms/blob/master/AddandSearchWord.java)
* [Identifying Strings](https://github.com/dengkliu/algorithms/blob/master/IdentifyingStrings.java)
### Segment Tree
### Binary Indexed Tree
### Heap (Priority Queue)
### Skip List

### General Data Structures

Here is a [time complexity analysis](https://github.com/dengkliu/algorithms/blob/master/ds) for all other general used data sturctures in java. 

## Tips
* First go through brute force approach
* Seek for optimal time complextiy you can achieve
  * If brute force is O(N), you should think about O(logn)
* StringBuilder is not thread safe, but StringBuffer is.
* Subarray is continuous, while subsquence is not. For an array with length N, there are N^2 subarrays and 2^N subsequences.
* Data Range can help with coming up with the time complexity of a solution. 10^6 - 10^9 is the boundary.
  * n = 10^4. You can do O(N) or O(NlogN) -- Two pointers? PrefixSum? DP?
  * n = 10^3. You can do O(N^2) -- Dynamic programming?
  * n = 10^2. You can do O(N^3) -- Three levels of for loop?
  * n = 10. You can do O(N!) -- DFS.
  * n = 10^9. You cannot even do O(N). You should be O(logN)


## Other coding questions
