# Algorithms (In Python)

## 1. Sorting 排序
Both of them use divide and conquer.
* [Quick sort](https://github.com/dengkliu/algorithms/blob/master/QuickSort.java)
* [Merge sort](https://github.com/dengkliu/algorithms/blob/master/MergeSort.java)

## 2. Binary Tree Traversal 二叉树遍历

With inorder and pre order/post order, you can rebuild a tree. With only pre order and post order, you cannot rebuild a tree.

* [Inorder Traveral of Binary Tree - Iterative Version ](https://github.com/dengkliu/algorithms/blob/master/InoderTraversal.java)
* [Preorder Traversal of Binary Tree - Iterative Version](https://github.com/dengkliu/algorithms/blob/master/PreorderTraversal.java)
* [Convert Binary Tree to Sorted Doubly Linked List](https://github.com/dengkliu/algorithms/blob/master/ConvertBinarySearchTreeToSortedDoublyLinkedList.java)
* [Flatten Binary Tree To Linked List](https://github.com/dengkliu/algorithms/blob/master/FlattenBinaryTreeToLinkedList.java)
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

Breath-First search (BFS) is often used to get topological order, to solve connectivity problem, to get shortest path or do level order traversal. BFS is also used to solve problem of counting steps from an original state to an end state given moving/transforming rules. This is the [Template](https://github.com/dengkliu/algorithms/blob/master/BFS.java) for BFS.

### Get Topological Order 拓扑排序

[Introduction](https://www.jianshu.com/p/b59db381561a) to topological order. For each node it has in-degree and out-degree. A node can be starting node if its in-degree is 0. After BFS, if the sequence length is equal to the total number of nodes, then there exists topological order for the graph. Only DAG (Directed Acyclic Graph) has topological order. 

BSF can be used to 1. find any topological order, 2. verify if there exists an topological order, 3. find the least topogical order in dictionary 4. find whether there exists just 1 topogical order.

* [Topological Sorting](https://github.com/dengkliu/algorithms/blob/master/TopologicalSorting.java)
* [Course Schedule](https://github.com/dengkliu/algorithms/blob/master/CourseSchedule.java)

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
* [The Maze III](https://github.com/dengkliu/algorithms/blob/master/TheMazeIII.java)
* [Sliding Puzzle](https://github.com/dengkliu/algorithms/blob/master/SlidingPuzzle.java)
* [Sliding Puzzle II](https://github.com/dengkliu/algorithms/blob/master/SlidingPuzzleII.java)
* [Zombie In Matrix](https://github.com/dengkliu/algorithms/blob/master/ZombieInMatrix.java)
* [Shortest Path Visiting All Nodes](https://github.com/dengkliu/algorithms/blob/master/ShortestPathVisitingAllNodes.java)
  
### Connectivity 连通性问题

Find all nodes that connect to a node in the graph.

* [Number of Big Islands](https://github.com/dengkliu/algorithms/blob/master/NumberOfBigIslands.java)
* [Lake Escape](https://github.com/dengkliu/algorithms/blob/master/LakeEscape.java)

### Others

You can also use BFS to 1. work on a 2D matrix problem regarding some maximum/minimum problems. Sometimes the problem can also be solved with DP. 2. find farthest node from a start, and furthermore find the two farthest nodes in a graph.

* [Map Jump](https://github.com/dengkliu/algorithms/blob/master/MapJump.java)
* [Longest path on a tree](https://github.com/dengkliu/algorithms/blob/master/LongestPathOnTheTree.py)
* [Second Diameter](https://github.com/dengkliu/algorithms/blob/master/second_diameter.py)

## 10. Depth-First Search 深度优先搜索

What is DFS for a graph? Start from a node, choose a neighbor and move on, until the end (no more child), if you reach the end, move back one step, and switch to another neigbor for current node, until you exhuast all the neigbors, the move back one more step and repeat. Keep searching for the target in this process, for one path you cannot revisit a node, but you can revisit the same node in a different path.

DFS is often used to solve tree problems using divide and conquer, to get all solutions to meet certain requirements, adn to solve combination & permutation/arrangement problems.

### Tree Traversal (Divide and Conquer)
* [Convert Binary Tree to Sorted Doubly Linked List](https://github.com/dengkliu/algorithms/blob/master/ConvertBinarySearchTreeToSortedDoublyLinkedList.java)
* [Flatten Binary Tree To Linked List](https://github.com/dengkliu/algorithms/blob/master/FlattenBinaryTreeToLinkedList.java)
* [Equal Tree Partition](https://github.com/dengkliu/algorithms/blob/master/EqualTreePartition.java)
* [The diameter of binary tree](https://github.com/dengkliu/algorithms/blob/master/DiameterOfBinaryTree.java)

### Find All Solutions 找到所有方案

* [Generate Parentheses](https://github.com/dengkliu/algorithms/blob/master/GenerateParentheses.java)
* [Couse Schedule IV](https://github.com/dengkliu/algorithms/blob/master/CourseScheduleIV.java)

### Combination & Permutation

Find all combinations and permutations that meet a certain requirement. Find one combination and permutation that meets a certain requirement. Find the optimal combination and permutation.

* [K Sum](https://github.com/dengkliu/algorithms/blob/master/KSum.java)
* [K Sum II](https://github.com/dengkliu/algorithms/blob/master/KSumII.java)
* [Word Squares](https://github.com/dengkliu/algorithms/blob/master/word_squares.py)
* [Factorization](https://github.com/dengkliu/algorithms/blob/master/factorization.py)
* [Subsets II](https://github.com/dengkliu/algorithms/blob/master/subset_II.py)

## 11. Dynamic Programming 动态规划

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection
of **simpler subproblems**, solving each of those subproblems **just once**, and **storing their solutions** 
using a memory-based data structure(array, map, etc). 

Trade the space complexity for time complexity.

### Coordinate DP
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* [Climbing Stairs](https://github.com/dengkliu/algorithms/blob/master/climbing_stairs.py)
* [Number of Ways to Stay in the Same Place After Some Steps II](https://github.com/dengkliu/algorithms/blob/master/number_of_ways_to_stay_in_same_place_after_some_steps_II.py)
* [Minimum Falling Path Sum](https://github.com/dengkliu/algorithms/blob/master/minimum_failing_path_sum.py)
* [Calculate the Sum of Path](https://github.com/dengkliu/algorithms/blob/master/calculate_the_sum_of_path.py)
* [Push Dominoes](https://github.com/dengkliu/algorithms/blob/master/push_dominoes.py)
* [Distinct Subsequences II](https://github.com/dengkliu/algorithms/blob/master/distinct_subsequences.py)
* [Subset II](https://github.com/dengkliu/algorithms/blob/master/subset_II.py)
* [Paint House](https://github.com/dengkliu/algorithms/blob/master/paint_house.py)
* [Decode Ways](https://github.com/dengkliu/algorithms/blob/master/decode_ways.py)
* [Decode Ways II](https://github.com/dengkliu/algorithms/blob/master/decode_ways_II.py)
* [Longest Increasing Subsequence](https://github.com/dengkliu/algorithms/blob/master/longest_increasing_subsequence.py)
* [Rat Jump](https://github.com/dengkliu/algorithms/blob/master/rat_jump.py)
* [Maximal Square](https://github.com/dengkliu/algorithms/blob/master/maximal_square.py)
* [Count Square Submatrices with All Ones](https://github.com/dengkliu/algorithms/blob/master/count_squares.py)

### Backpack DP 
* [Backpack](https://github.com/dengkliu/algorithms/blob/master/backpack.py)
* [Backpack II](https://github.com/dengkliu/algorithms/blob/master/backpack_II.py)
* [Backpack III](https://github.com/dengkliu/algorithms/blob/master/backpack_III.py)
* [Backpack IV](https://github.com/dengkliu/algorithms/blob/master/backpack_IV.py)
* [Backpack V](https://github.com/dengkliu/algorithms/blob/master/backpack_V.py)
* [Backpack VII](https://github.com/dengkliu/algorithms/blob/master/backpack_VII.py)
* [Backpack VIII](https://github.com/dengkliu/algorithms/blob/master/backpack_VIII.py)
* [Backpack IX](https://github.com/dengkliu/algorithms/blob/master/backpack_IX.py)
* [Backpack X](https://github.com/dengkliu/algorithms/blob/master/backpack_X.py)
* [Partition Equal Subset Sum](https://github.com/dengkliu/algorithms/blob/master/partition_equal_subset_sum.py)
* [Best Time to Buy and Sell Stock III](https://github.com/dengkliu/algorithms/blob/master/BestTimeToBuyAndSellStockIII.java)
* [K Sum](https://github.com/dengkliu/algorithms/blob/master/KSum.java)
* [K Sum II](https://github.com/dengkliu/algorithms/blob/master/KSumII.java)
* [Card Game](https://github.com/dengkliu/algorithms/blob/master/card_game.py)
* [Profitable Schemes](https://github.com/dengkliu/algorithms/blob/master/profitable_schemes.py)
* [Float Combination Sum](https://github.com/dengkliu/algorithms/blob/master/float_combination_sum.py)

### Interval DP
* [Stone Game](https://github.com/dengkliu/algorithms/blob/master/stone_game.py)
* [Stone Game II](https://github.com/dengkliu/algorithms/blob/master/stone_game_II.py)
* [Minimum Cost to Merge Stones](https://github.com/dengkliu/algorithms/blob/master/minimum_cost_to_merge_stones.py)

### Prefix DP
* [Longest Common Subsequence](https://github.com/dengkliu/algorithms/blob/master/LongestCommonSubsequence.java)


## 12. Monotonic Stack/Queue

* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/ShortedSubarraySumAtLeastK.java)

## 13. Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## 14. Useful data structures
### Union Find
[Union Find](https://github.com/dengkliu/algorithms/blob/master/union_find.py) is used to solve connection problem, especially for dynamic data stream (online algorithm). BFS can only be used to solve connection problem for static data (therefore BFS is offline algorithm), for data stream, the time complexity will be horrible.

* Union Find support O(1) time to merge two set which contains x and y - merge(x,y)
* Union Find support O(1) time to query the set that contains x - find(x)
* Union Find support O(1) time to query whether x and y are in the same set - isConnected(x,y)

The internal structure of Union Find is multiple multi-way trees. Each child node points to a father node. Each root corresponds to a set. We use a hashmap/dictionary to map a child to a father. With this tree structure, we can do:
* Move upward to the root to find the set that contains an element - find(x)
* Check if two element belongs to the same set - have the same root - find(x) == find(y)
* Merget the set of x and set of y, set the parent of find(x) to find(y)

Related coding questions
  * [Connecting Graph](https://github.com/dengkliu/algorithms/blob/master/connecting_graph.py)
  * [Connecting Graph II](https://github.com/dengkliu/algorithms/blob/master/connecting_graph_II.py)
  * [Connecting Graph III](https://github.com/dengkliu/algorithms/blob/master/connecting_graph_III.py)
  * [Graph Validate Tree I](https://github.com/dengkliu/algorithms/blob/master/graphy_valid_tree.py)
  * [Graph Validate Tree II](https://github.com/dengkliu/algorithms/blob/master/graph_valid_tree_II.py)
  * [Set Union](https://github.com/dengkliu/algorithms/blob/master/set_union.py)
  * [Account Merge](https://github.com/dengkliu/algorithms/blob/master/account_merge.py)
  * [Maximum Connected Area](https://github.com/dengkliu/algorithms/blob/master/MaximumConnectedArea.java)
  * [Maximum Association Set](https://github.com/dengkliu/algorithms/blob/master/maximum_association_set.py)
  * [Number of Islands II](https://github.com/dengkliu/algorithms/blob/master/number_of_islands_II.py)

### Trie

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
