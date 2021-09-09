# Algorithms

## 1. Sorting 排序
Both of them use divide and conquer.
* [Quick sort](https://github.com/dengkliu/algorithms/blob/master/QuickSort.java)
* [Merge sort](https://github.com/dengkliu/algorithms/blob/master/MergeSort.java)

## 2. Binary Tree Traversal 二叉树遍历

* [Inorder Traveral of Binary Tree - Iterative Version ](https://github.com/dengkliu/algorithms/blob/master/InoderTraversal.java)
* [Convert Binary Tree to Sorted Doubly Linked List](https://github.com/dengkliu/algorithms/blob/master/ConvertBinarySearchTreeToSortedDoublyLinkedList.java)
* [Kth Smallest Element in BST](https://github.com/dengkliu/algorithms/blob/master/KthSmallestElementInBST.java)

## 3. Binary Tree Divide & Conquer 二叉树分治
* [Binary Tree Maximum Path Sum](https://github.com/dengkliu/algorithms/blob/master/BinaryTreeMaximumPathSum.java)
* [Validate Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/ValidateBinarySearchTree.java)

## 4. Greedy 贪心算法

* [Best Time to Buy and Sell Stock](https://github.com/dengkliu/algorithms/blob/master/BestTimeToBuyAndSellStock.java)
* [Best Time to Buy and Sell Stock II](https://github.com/dengkliu/algorithms/blob/master/BestTimeToBuyAndSellStockII.java)

## 5. Prefix Sum 前缀和
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**. 

The definition of prefix sum for 1D and 2D array.
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/PrefixSum.java) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefixSum2Dimention.java)

Related coding problems.
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/MaximumSubarray.java)
* [Subarray Sum Equals K](https://github.com/dengkliu/algorithms/blob/master/SubarraySumEqualK.java)
* [Shortest Subarray Sum Equals to K](https://github.com/dengkliu/algorithms/blob/master/ShortestSubarraySumEqualK.java)
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/ShortedSubarraySumAtLeastK.java)
* [Matrix Restoration](https://github.com/dengkliu/algorithms/blob/master/MatrixRestoration.java)
* [Product of Array Except Itself](https://github.com/dengkliu/algorithms/blob/master/ProductOfArrayExceptSelf.java)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java)
* [Subarray Sum II](https://github.com/dengkliu/algorithms/blob/master/SubarraySumII.java)
* [Binary Subarrays With Sum](https://github.com/dengkliu/algorithms/blob/master/BinarySubarraysWithSum.java)

## 6. Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

* [Number of Airplanes in the Sky](https://github.com/dengkliu/algorithms/blob/master/NumberOfAirplanesInTheSky.java)

## 7. Two Pointers 双指针

Two pointers are usually used when:
* Sliding window problem
* Time complexity is O(N) (80%)
* In-place algorithm, you can not use extra space.
* Subarray or substring problem (50%)
* Palindrome problem (50%)

### [Same direction two pointers](https://github.com/dengkliu/algorithms/blob/master/SameDirectionTwoPointers.java) 同向双指针
Two pointers start from the head of array and go to the end. 同向双指针只能用于一种条件，那就是解存在一种单调性，当右移左指针的时候，右指针不应该往回走，为了找到结，右指针只能继续往右走。

* [Minimum Size Subarray Sum](https://github.com/dengkliu/algorithms/blob/master/MinimumSizeSubarray.java)
* [Substring With At Least K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/SubstringWithAtLeastKDistinctCharacters.java)
* [Minimum Window Substring](https://github.com/dengkliu/algorithms/blob/master/MinimumWindowSubstring.java)
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/Heaters.java)
* [Longest Substring Without Repeating Characters](https://github.com/dengkliu/algorithms/blob/master/LongestSubstringWithoutRepeatingCharacters.java)
* [Longest Substring With At Most K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/LongestSubstringWithAtMostKDistinctCharacters.java)
* [Binary Subarrays With Sum](https://github.com/dengkliu/algorithms/blob/master/BinarySubarraysWithSum.java)

### Fixed Size Sliding Window 固定长度滑动窗口

* [Grumpy Bookstore Owner](https://github.com/dengkliu/algorithms/blob/master/GrumpyBookStoreOwner.java)
* [Pick Apples](https://github.com/dengkliu/algorithms/blob/master/PickApples.java)

### Opposite direction two pointers 相向双指针
* [Two Sim VII](https://github.com/dengkliu/algorithms/blob/master/TwoSumVII.java)
### Back direction two pointers 背向双指针
* [Shortest Palindrome](https://github.com/dengkliu/algorithms/blob/master/ShortestPalindrome.java)

## 8. Binary Search 二分查询

You may want to use binary search when -
* When the interviewer ask you to find a solution that is better than O(N)
* Find a cut in the array, which makes the left half meet the condition, the other half don't.
* The array is sorted, find a global maximum or minimum value to meet a certain requirement
* Find a local minimum or maximum.

Related coding problem -

* [Maximum Number in Mountain Sequence](https://github.com/dengkliu/algorithms/blob/master/MaximumNumberInMountainSequence.java)
* [Find word](https://github.com/dengkliu/algorithms/blob/master/FindWords.java)
* [Search in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/SearchInRotatedSortedArray.java)
* [Wood Cut](https://github.com/dengkliu/algorithms/blob/master/WoodCut.java)
* [Copy Books](https://github.com/dengkliu/algorithms/blob/master/CopyBooks.java)
* [Find K Closet Elements](https://github.com/dengkliu/algorithms/blob/master/FindKClosestElements.java)
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/Heaters.java)
* [Find Peak Element II](https://github.com/dengkliu/algorithms/blob/master/FindPeakElementII.java)

## 9. Breath-First Search 宽度优先搜索

Breath-First search (BFS) is often used to get topological order, to solve connectivity problem, to get shortest path or do level order traversal. BFS is also used to solve problem of counting steps to an end given moving/transforming rules. This is the [Template](https://github.com/dengkliu/algorithms/blob/master/BFS.java) for BFS.

### Get Topological Order 拓扑排序

[Introduction](https://www.jianshu.com/p/b59db381561a) to topological order. For each node it has in-degree and out-degree. A node can be starting node if its in-degree is 0. After BFS, if the sequence length is equal to the total number of nodes, then there exists topological order for the graph. Only DAG (Directed Acyclic Graph) has topological order. 

BSF can be used to 1. find any topological order, 2. verify if there exists an topological order, 3. find the least topogical order in dictionary 4. find whether there exists just 1 topogical order.

* [Topological Sorting](https://github.com/dengkliu/algorithms/blob/master/TopologicalSorting.java)

### Get Shortest Path 最短路径

BSF can be used to get shortest path in a simple graph. What is a simple graph? A graph is simple if 
* The edges have no direction.
* There are no weights on edges. 
* There can be at most 1 edge between 2 nodes.
* One node can not have an edge to itself. (No graph loop)

BSF can be enhanced to Shortest Path Fatser Algorithm (SPFA) to get shortest path in a complex graph. In a simple graph, the shortest path to a node is simply the number of levels that it take to reach this node. In a complex graph, you may find a node with shorter distance but appears to be in deeper level.

How does SPFA solve this problem? If we find a node in level 3 that has been visited in level 2 but now we find a shorter distance, then we throw this node back to  the queue.

* [Build Post Office II](https://github.com/dengkliu/algorithms/blob/master/BuildPostOfficeII.java)
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* [Maze III]()
  
### Connectivity 连通性问题

Find all nodes that connect to a node in the graph.

* Longest path on a tree - https://www.lintcode.com/problem/1469

## 10. Depth-First Search 深度优先搜索
* Divide and Conquer.
  * What should be returned form next level?
  * What is the result at each level?
### 1）Coding Problems
* The diameter of binary tree - https://www.lintcode.com/problem/1181

## 11. Dynamic Programming 动态规划

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection
of **simpler subproblems**, solving each of those subproblems **just once**, and **storing their solutions** 
using a memory-based data structure(array, map, etc). 

Trade the space complexity for time complexity.

### 1）Coordinate DP
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* Climbing Stairs
* Rat Jump - https://www.lintcode.com/problem/1861/ 

### 2）Backpack DP 
* [Best Time to Buy and Sell Stock III](https://github.com/dengkliu/algorithms/blob/master/BestTimeToBuyAndSellStockIII.java)
* Float Combination Sum https://www.lintcode.com/problem/1800/
* Longest Common Subsequence - https://www.lintcode.com/problem/77/
* Longest Increasing Subsequence

### 3）Interval DP
* Related coding questions
* Stone Game - https://www.lintcode.com/problem/476/

### 4) Prefix DP
* Related coding questions
* [Longest Common Subsequence](https://github.com/dengkliu/algorithms/blob/master/LongestCommonSubsequence.java)

## 12. Monotonic Stack/Queue

### Coding problems
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/ShortedSubarraySumAtLeastK.java)

## 13. Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## 14. Useful data structures
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
