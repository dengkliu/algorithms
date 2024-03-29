# Algorithms (In Python)

## 1. Tree

### 1.1 Binary Tree Traversal

#### 1.1.1 Pre/In/Post Order Traversal

* [Binary Tree Preorder](https://github.com/dengkliu/algorithms/blob/master/pre_order_traversal_bst.py)
* [Flatten Binary Tree To Linked List](https://github.com/dengkliu/algorithms/blob/master/flatten_binary_tree_to_linkedlist.py)
* [Binary Tree Inorder](https://github.com/dengkliu/algorithms/blob/master/inorder_traversal_bst.py)
* [Kth Smallest Element in BST](https://github.com/dengkliu/algorithms/blob/master/kth_smallest_element_in_bst.py)
* [Convert Binary Search Tree to Sorted Doubly Linked List](https://github.com/dengkliu/algorithms/blob/master/convert_binary_search_tree_to_sorted_doubly_linked_list.py)
* [Binary Tree Postorder](https://github.com/dengkliu/algorithms/blob/master/post_order_traversal_bst.py)

#### 1.1.2 Level Order Traversal
* [Binary Tree Level Order Traversal](https://github.com/dengkliu/algorithms/blob/master/binary_tree_level_order_traversal.py)
* [Binary Tree Level Order Traversal II](https://github.com/dengkliu/algorithms/blob/master/binary_tree_level_order_traversal_ii.py)
* [Binary Tree Vertical Order Traversal](https://github.com/dengkliu/algorithms/blob/master/binary_tree_vertical_order_traversal.py)
* [Binary Tree Right Side View](https://github.com/dengkliu/algorithms/blob/master/binary_tree_right_side_view.py)
* [Find Largest Value in Each Tree Row](https://github.com/dengkliu/algorithms/blob/master/binary_tree_find_largest_value_in_each_tree_row.py)

### 1.2 Tree Divide & Conquer (Depth First Search)
* [Invert Binary Tree](https://github.com/dengkliu/algorithms/blob/master/invert_binary_tree.py)
* [Binary Tree Paths](https://github.com/dengkliu/algorithms/blob/master/binary_tree_paths.py)
* [Validate Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/validate_binary_search_tree.py)
* [Lowest Common Ancestor of a Binary Tree](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor.py)
* [Lowest Common Ancestor of a Binary Tree II](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_ii.py)
* [Lowest Common Ancestor of a Binary Tree III](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_iii.py)
* [Lowest Common Ancestor of a Binary Tree IV](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_iv.py)
* [Construct String from Binary Tree](https://github.com/dengkliu/algorithms/blob/master/construct_string_from_binary_tree.py)
* [Delete Nodes and Return Forest](https://github.com/dengkliu/algorithms/blob/master/delete_nodes_and_return_forest.py)
* [Delete Node in a BST](https://github.com/dengkliu/algorithms/blob/master/delete_node_in_a_bst.py)
* [Delete Subtree that Sum to 0](https://github.com/dengkliu/algorithms/blob/master/delete_tree_nodes.py)
* [Count Nodes Equals to Average of Subtree](https://github.com/dengkliu/algorithms/blob/master/count_nodes_equals_to_average_of_subtree.py)
* [Symmetric Tree](https://github.com/dengkliu/algorithms/blob/master/symmetric_tree.py)
* [Equal Tree Partition](https://github.com/dengkliu/algorithms/blob/master/equal_tree_partition.py)
* [Serialize and Deserialize Binary Tree](https://github.com/dengkliu/algorithms/blob/master/serialize_and_deserialize_binary_tree.py)
* [Serialize and Deserialize N-ary Tree](https://github.com/dengkliu/algorithms/blob/master/serialize_and_deserialize_n_ary_tree.py)
* [Binary Tree Maximum Path Sum](https://github.com/dengkliu/algorithms/blob/master/binary_tree_maximum_path_sum.py)
* [Construct Binary from Preorder and Inorder Traversal](https://github.com/dengkliu/algorithms/blob/master/construct_binary_tree_from_preorder_and_inoder_traversal.py)

#### 1.2.1 Tree's Height
* [Diameter of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/DiameterOfBinaryTree.java)
* [Number of Good Leaf Nodes Pairs](https://github.com/dengkliu/algorithms/blob/master/num_of_good_leaf_nodes_pairs.py)
* [Find leaves of binary tree](https://github.com/dengkliu/algorithms/blob/master/find_leaves_of_binary_tree.py)
* [Height of Binary Tree after Subtree Removal Queries](https://github.com/dengkliu/algorithms/blob/master/height_of_binary_tree_after_subtree_removal_queries.py)

## 2. Breath-First Search

[BFS Template](https://github.com/dengkliu/algorithms/blob/master/breadth_first_search.py)

### 2.1 Connectivity

* [Island Perimeter](https://github.com/dengkliu/algorithms/blob/master/island_perimeter.py)
* [Number of Islands](https://github.com/dengkliu/algorithms/blob/master/number_of_islands.py)
* [Number of Big Islands](https://github.com/dengkliu/algorithms/blob/master/NumberOfBigIslands.java)
* [Lake Escape](https://github.com/dengkliu/algorithms/blob/master/LakeEscape.java)
* [Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/description/)

### 2.2 Get Shortest Path

BSF can be used to get shortest path in a simple graph. What is a simple graph? A graph is simple if 
* The edges have no direction.
* There are no weights on edges. 
* There can be at most 1 edge between 2 nodes.
* One node can not have an edge to itself. (No graph loop)

BSF can be enhanced to Shortest Path Fatser Algorithm (SPFA) to get shortest path in a complex graph. In a simple graph, the shortest path to a node is simply the number of levels that it take to reach this node. In a complex graph, you may find a node with shorter distance but appears to be in deeper level.

How does SPFA solve this problem? If we find a node in level 3 that has been visited in level 2 but now we find a shorter distance, then we throw this node back to  the queue.

* [Build Post Office II](https://github.com/dengkliu/algorithms/blob/master/build_post_office.py) 
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* [The Maze](https://github.com/dengkliu/algorithms/blob/master/the_maze.py)
* [The Maze II](https://github.com/dengkliu/algorithms/blob/master/the_maze_ii.py)
* [The Maze III](https://github.com/dengkliu/algorithms/blob/master/the_maze_iii.py) 
* [Sliding Puzzle](https://github.com/dengkliu/algorithms/blob/master/sliding_puzzle.py) 
* [Sliding Puzzle II](https://github.com/dengkliu/algorithms/blob/master/SlidingPuzzleII.java) 
* [Zombie In Matrix](https://github.com/dengkliu/algorithms/blob/master/ZombieInMatrix.java)
* [Shortest Path Visiting All Nodes](https://github.com/dengkliu/algorithms/blob/master/ShortestPathVisitingAllNodes.java)

### 2.3 Get Topological Order

[Introduction](https://www.jianshu.com/p/b59db381561a) to topological order. For each node it has in-degree and out-degree. A node can be starting node if its in-degree is 0. After BFS, if the sequence length is equal to the total number of nodes, then there exists topological order for the graph. Only DAG (Directed Acyclic Graph) has topological order. 

BSF can be used to 1. find any topological order, 2. verify if there exists an topological order, 3. find the least topogical order in dictionary 4. find whether there exists just 1 topogical order.

* [Topological Sorting](https://github.com/dengkliu/algorithms/blob/master/topological_sorting.py) 
* [Course Schedule](https://github.com/dengkliu/algorithms/blob/master/course_schedule.py)
* [Course Schedule II](https://github.com/dengkliu/algorithms/blob/master/course_schedule_ii.py)

### Others

You can also use BFS to 1. work on a 2D matrix problem regarding some maximum/minimum problems. Sometimes the problem can also be solved with DP. 2. find farthest node from a start, and furthermore find the two farthest nodes in a graph.

* [Map Jump](https://github.com/dengkliu/algorithms/blob/master/MapJump.java)
* [Longest path on a tree](https://github.com/dengkliu/algorithms/blob/master/LongestPathOnTheTree.py)
* [Second Diameter](https://github.com/dengkliu/algorithms/blob/master/second_diameter.py)

## 3. Depth-First Search

What is DFS for a graph? Start from a node, choose a neighbor and move on, until the end (no more child), if you reach the end, move back one step, and switch to another neigbor for current node, until you exhuast all the neigbors, the move back one more step and repeat. Keep searching for the target in this process, for one path you cannot revisit a node, but you can revisit the same node in a different path. 

DFS is often used to (1) solve tree problems using divide and conquer, (2) to get all solutions to meet certain requirements, and (3) to solve combination & permutation/arrangement problems. 

For (2) and (3), a technique called **backtracking** is often used. Backtracking involves DFS but with the additional strategy of pruning branches that violate constraints or cannot lead to a solution. It is a systematic method for solving problems by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the number of steps taken to reach that level.

### Tree Traversal (Divide and Conquer)

Find tree's problems [above](https://github.com/dengkliu/algorithms/blob/master/README.md#12-tree-divide--conquer-depth-first-search).

### Find All Solutions 

Find all solutions that meet a certain requirement; find a specific solution that meets the certain requirement. 

* [Generate Parentheses](https://github.com/dengkliu/algorithms/blob/master/generate_parentheses.py)
* [Couse Schedule IV](https://github.com/dengkliu/algorithms/blob/master/CourseScheduleIV.java)
* [Word Search II](https://github.com/dengkliu/algorithms/blob/master/word_search_II.py)

### Combination & Permutation

Find all combinations and permutations that meet a certain requirement. Find one combination and permutation that meets a certain requirement. Find the optimal combination and permutation.

* [K Sum](https://github.com/dengkliu/algorithms/blob/master/KSum.java)
* [K Sum II](https://github.com/dengkliu/algorithms/blob/master/KSumII.java)
* [Word Squares](https://github.com/dengkliu/algorithms/blob/master/word_squares.py)
* [Factorization](https://github.com/dengkliu/algorithms/blob/master/factorization.py)
* [Subsets II](https://github.com/dengkliu/algorithms/blob/master/subset_II.py)

## 4. Greedy 贪心算法

* [Best Time to Buy and Sell Stock](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock.py)
* [Best Time to Buy and Sell Stock II](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock_II.py)
* [Best Time to Buy and Sell Stock V](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock_V.py)

## 5. Prefix Sum 前缀和
Prefix sum is mostly used for getting the subarray sum, if the subarray is **immutable**. 

The definition of prefix sum for 1D and 2D array.
* [1 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefix_sum.py) 
* [2 dimentional array](https://github.com/dengkliu/algorithms/blob/master/prefix_sum_two_dimension.py)

Related coding problems.
* [Maximum Subarray](https://github.com/dengkliu/algorithms/blob/master/maximum_subarray.py) ✅ 通过确定之前的区间最小值，来获取当前的区间最大值，打擂台。
* [Shortest Subarray Sum Equals to K](https://github.com/dengkliu/algorithms/blob/master/shortest_subarray_sum_equal_k.py) ✅ 经典题，区间和问题！数组元素可正可负（排除双指针解法），而且是确定数值的区间和（map记录区间和to数组元素，因为是求最短，相同的sum，index直接覆盖之前的index）！），要找最短，枚举subarray的end, 打擂台。
* [Subarray Sum Equals K](https://github.com/dengkliu/algorithms/blob/master/subarray_sum_equal_k.py) ✅ 确定数值的区间和问题，数组元素可正可负（排除双指针解法），枚举区间右端点，用map记录之前的和与位置，因为负数的存在，同一个和可能对应多个位置。
* [Binary Subarrays With Sum](https://github.com/dengkliu/algorithms/blob/master/binary_subarrays_with_sum.py) ✅ 确定数值区间和的特例。
* [Matrix Restoration](https://github.com/dengkliu/algorithms/blob/master/MatrixRestoration.java) ✅ 在二维数组上的Prefix sum应用
* [Product of Array Except Itself](https://github.com/dengkliu/algorithms/blob/master/ProductOfArrayExceptSelf.java) ✅ Prefix product。从尾部开始处理。
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java)
* [Subarray Sum II](https://github.com/dengkliu/algorithms/blob/master/subarray_sum_II.py) ✅ Prefix sum, 全部是postive number，所以可以用双指针。

## 5. Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

* [Number of Airplanes in the Sky](https://github.com/dengkliu/algorithms/blob/master/number_of_airplanes_in_the_sky.py) ✅ 解决区间问题的经典题，把起点和终点分别flag，在时间上进行排序。

## 6. Two Pointers 双指针

Two pointers are usually used when:
* Sliding window problem
* Time complexity is O(N) (80%)
* In-place algorithm, you can not use extra space.
* Subarray or substring problem (50%)
* Palindrome problem (50%)

### [Same direction two pointers](https://github.com/dengkliu/algorithms/blob/master/same_direction_two_pointers.py) 同向双指针
Two pointers start from the head of array and go to the end. 同向双指针只能用于一种条件，那就是解存在一种单调性，当起始指针右移的时候，终止指针不应该往回走，为了找到结，右指针只能继续往右走。底层逻辑就是-->如果一个子数组不满足条件，那么这个子数组的所有子数组均不满足条件。

* [Minimum Size Subarray Sum](https://github.com/dengkliu/algorithms/blob/master/minimum_size_of_subarray.py)
* [Substring With At Least K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/substring_with_at_least_K_distinct_characters.py) ✅ 枚举起点，找到每个起点所有满足条件的情况
* [Minimum Window Substring](https://github.com/dengkliu/algorithms/blob/master/MinimumWindowSubstring.java) ✅ 枚举起点。用到dictionary去记录次数，记住只有正好cover的时候才更新coverred characters。
* [Longest Substring Without Repeating Characters](https://github.com/dengkliu/algorithms/blob/master/longest_substring_without_repeating_characters.py) ✅ 枚举起点，找寻终点。Python set(iterable) 去查重
* [Longest Substring With At Most K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/LongestSubstringWithAtMostKDistinctCharacters.java) ✅ 枚举起点，用dictionary记录characters出现次数，只有当次数为0时，才去掉这个character.
* [Subarray Sum II](https://github.com/dengkliu/algorithms/blob/master/subarray_sum_II.py) ✅ Prefix sum, 全部是postive number，所以可以用双指针。

### Fixed Size Sliding Window 固定长度滑动窗口

* [Grumpy Bookstore Owner](https://github.com/dengkliu/algorithms/blob/master/GrumpyBookStoreOwner.java) ✅ Slding window经典题，枚举终点，注意第一个初始状态window的位置，初始化的时候直接assume window在这个位置，求得一个解，然后移动window，打擂台。
* [Pick Apples](https://github.com/dengkliu/algorithms/blob/master/PickApples.java) ✅ 典型的fixed size sliding window + 双字段问题。注意双字段问题可以用隔板法，隔板法用for loop,隔板位置从0到n-1，[0, i) [i, n-1], 在子函数里 start - end <= 0 或者 window size直接返回-1.

### Opposite direction two pointers 相向双指针
* [Two Sim VII](https://github.com/dengkliu/algorithms/blob/master/TwoSumVII.java) ✅ two pointer的升级版，基本思路一样，只是需要找到start下一个更大的数和end上一个更小的数。
### Back direction two pointers 背向双指针
* [Shortest Palindrome](https://github.com/dengkliu/algorithms/blob/master/ShortestPalindrome.java) ✅ check palindrome 经典问题，每个位置注意check两种情况。

## 7. Binary Search 二分查询

You may want to use binary search when -
* When the interviewer ask you to find a solution that is better than O(N)
* Find a cut in the array, which makes the left half meet the condition, the other half don't.
* The array is sorted, find a global maximum or minimum value to meet a certain requirement
* Find a local minimum or maximum.

Related coding problem -

* [Maximum Number in Mountain Sequence](https://github.com/dengkliu/algorithms/blob/master/maximum_number_in_mountain_sequence.py)
* [Find in Mountain Array](https://github.com/dengkliu/algorithms/blob/master/find_in_mountain_array.py)
* [H-Index II](https://github.com/dengkliu/algorithms/blob/master/h_index_ii.py)
* [Find word](https://github.com/dengkliu/algorithms/blob/master/find_words.py) ✅ - 二分法在有序数列中找一个target的下一个/前一个接近的数
* [Search in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/search_in_rotated_sorted_array.py) ✅ - 二分法先找到分界点，思考分界点两边的数字有什么不同？（分界点左边都比第一个数字大，右边都比第一个数字小），找到分界点之后，根据现在target确定搜索的范围。
* [Wood Cut](https://github.com/dengkliu/algorithms/blob/master/wood_cut.py) ✅ - 确定解的范围，在这个范围中尝试，如果能行，就试试更大的值，不行就试试更小的。
* [Copy Books](https://github.com/dengkliu/algorithms/blob/master/copy_books.py) ✅ - 跟上面题一样的思路，确定解的范围，在这个范围中尝试，如果人够，就试试更小的值（人会要的更多），不行就试试更大的。
* [Find K Closet Elements](https://github.com/dengkliu/algorithms/blob/master/find_k_closet_elements.py) ✅ - 跟find word题类似，先找到离target最接近的数字，然后再用two pointer往两边扩展。
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/heaters.py) ✅ - 对于每个房子，找到最近的heater（还是find word的套路），看看radius是多少，持续更新最大radius(打擂台)
* [Find Peak Element II](https://github.com/dengkliu/algorithms/blob/master/find_peak_element_II.py) ✅ - 二分法找local极值，数列不是sort的，但是也可以用来找local极值！！
* [Median of Two Sorted Array](https://github.com/dengkliu/algorithms/blob/master/median_of_two_sorted_arrays.py)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java) 
* [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

## 10. Dynamic Programming 动态规划

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
* [Longest Common Subsequence](https://github.com/dengkliu/algorithms/blob/master/longest_common_sequence.py)
* [Height of Binary Tree after Subtree Removal Queries](https://github.com/dengkliu/algorithms/blob/master/height_of_binary_tree_after_subtree_removal_queries.py)

## 11. Monotonic Stack/Queue

Monotonic stack is an algorithm that is implemented based on stack. 
The elements in the stack are sorted by a certain rule (usually number comparison). 
Monotonic stack is often used to find the first smaller or larger item on the left or right of the current.
Its time complexity is O(N).

Stack that is monotone increasing can be used to find the first element that is less than current element on the left and right.
Stack that is monotone decreasing can be used to find the first element that is larger than current element on the left and right.

* [Largest Rectangle in Histogram](https://github.com/dengkliu/algorithms/blob/master/largest_rectangle_in_histogram.py)
* [Maximal Rectange](https://github.com/dengkliu/algorithms/blob/master/maximal_rectangle.py)
* [Max Tree](https://github.com/dengkliu/algorithms/blob/master/max_tree.py)
* [Final Discount Price](https://github.com/dengkliu/algorithms/blob/master/final_discounted_price.py)
* [Tall Building](https://github.com/dengkliu/algorithms/blob/master/tall_buildings.py)
* [Sliding Window Maximum](https://github.com/dengkliu/algorithms/blob/master/sliding_window_maximum.py)
* [Shortest Subarray Sum At Least K](https://github.com/dengkliu/algorithms/blob/master/shortest_subarray_with_sum_at_least_K.py)

## 12. Others
* Greatest Common Divisor - https://www.lintcode.com/problem/845/
* Factorization - https://www.lintcode.com/problem/652/
* https://www.lintcode.com/problem/1877

## 13. Useful data structures
### Singly Linked List
* [Reverse Linked List](https://github.com/dengkliu/algorithms/blob/master/reverse_singly_linked_list.py)
### Double Linked List
* [LRU Cache](https://leetcode.com/problems/lru-cache/)

### Stack
* [Minimal Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
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
  * [Bricks Falling When Hit](https://github.com/dengkliu/algorithms/blob/master/bricks_falling_when_hit.py)

### Trie

[Trie](https://github.com/dengkliu/algorithms/blob/master/Trie.java) is used to store strings while compressing the string common prefix. Its internal structure is a tree. The more common prefixes shared by the words in the dictionary, the more time saved. 

The best time complexity for insert word and find word is O(L).

Trie is tested with problems including :
* Check if a prefix or word exists in Trie
* DFS on a Trie
* Optimize other algorithms with Trie

The structure of Trie -
* The character is stored on edges
* The word is stored on nodes

The more common prefixes in the trie, the more optimization we achieve. Every time we add a word, or search a word, the best time complexity is O(L), where L is the length of the word (search in dictionary is O(1)). The worst case we still need to traverse the entire tree.

Related coding questions
* [Add and Search Word - Data structure design](https://github.com/dengkliu/algorithms/blob/master/add_and_search_word_data_structure_design.py)
* [Identifying Strings](https://github.com/dengkliu/algorithms/blob/master/IdentifyingStrings.java)
* [Letter Combination of a Phone Number II](https://github.com/dengkliu/algorithms/blob/master/letter_combinations_of_a_phone_number.py)
* [Max Distance](https://github.com/dengkliu/algorithms/blob/master/max_distance.py)
* [Word Search II](https://github.com/dengkliu/algorithms/blob/master/word_search_II.py)
* [Word Search III](https://github.com/dengkliu/algorithms/blob/master/word_search_III.py)

### Segment Tree
### Binary Indexed Tree
### Heap (Priority Queue)
In Python, you need to import heapq library, and use heapq.heappop(heap) and heap.heappush(heap, element) to do pop and push operation.
* [Minimum Cost to Hire_K_Workers](https://github.com/dengkliu/algorithms/blob/master/minimum_cost_to_hire_K_workers.py)
* [Sliding Window Minimum]()

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
* [Math] [Nth Digit](https://github.com/dengkliu/algorithms/blob/master/nth_digit.py)

## Templates 模板
* [Python Coding Stype Guide](https://github.com/dengkliu/algorithms/blob/master/python_coding_style_guide.py)
* [Binary Search](https://github.com/dengkliu/algorithms/blob/master/binary_search_template.py) ✅
* [Two pointers](https://github.com/dengkliu/algorithms/blob/master/two_pointers.py)
* [Binary Tree Divide and Conquer](https://github.com/dengkliu/algorithms/blob/master/binary_tree_divide_and_conquer.py)
* [Quick sort](https://github.com/dengkliu/algorithms/blob/master/quick_sort.py)
* [Merge sort](https://github.com/dengkliu/algorithms/blob/master/merge_sort.py)
