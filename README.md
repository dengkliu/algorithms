
# Algorithms and Data Structures

## 0. General Tips
* First go through brute force approach.
* Seek for optimal time complextiy you can achieve, if brute force is O(N), you should think about O(logn)
* Data Range can help with coming up with the time complexity of a solution. 10^6 - 10^9 is the boundary.
  * n = 10^4. You can do O(N) or O(NlogN)
  * n = 10^3. You can do O(N^2) 
  * n = 10^2. You can do O(N^3) 
  * n = 10. You can do O(N!)
  * n = 10^9. You cannot even do O(N). You should be O(logN)
* Here is a [time complexity analysis](https://github.com/dengkliu/algorithms/blob/master/ds) for general used data sturctures in python. 

## 1. Tree
### 1.1 Tree Traversal
#### 1.1.1 Pre/In/Post Order Traversal

* [Binary Tree Preorder](https://github.com/dengkliu/algorithms/blob/master/pre_order_traversal_bst.py)
* [Flatten Binary Tree To Linked List](https://github.com/dengkliu/algorithms/blob/master/flatten_binary_tree_to_linkedlist.py)
* [Recover a Tree from Preorder Traversal with Dashes](https://github.com/dengkliu/algorithms/blob/master/recover_a_tree_from_preorder_traversal.py)
* [Boundary of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/boundary_of_binary_tree.py)
* [Binary Tree Inorder](https://github.com/dengkliu/algorithms/blob/master/inorder_traversal_bst.py)
* [Range Sum of Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/range_sum_of_bst.py)
* [Balance Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/balance_binary_search_tree.py)
* [Kth Smallest Element in BST](https://github.com/dengkliu/algorithms/blob/master/kth_smallest_element_in_bst.py)
* [Find Mode in Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/find_mode_in_binary_search_tree.py)
* [Convert Binary Search Tree to Sorted Doubly Linked List](https://github.com/dengkliu/algorithms/blob/master/convert_binary_search_tree_to_sorted_doubly_linked_list.py)
* [Binary Search Tree Iterator](https://github.com/dengkliu/algorithms/blob/master/binary_search_tree_iterator.py)
* [Closest Bianry Search Value](https://github.com/dengkliu/algorithms/blob/master/closest_binary_search_tree_value.py)
* [Binary Tree Postorder](https://github.com/dengkliu/algorithms/blob/master/post_order_traversal_bst.py)
* [Minimum Time to Collect All Apples in Tree](https://github.com/dengkliu/algorithms/blob/master/minimum_time_to_collect_all_apples_in_a_tree.py)

#### 1.1.2 Level Order Traversal
* [Binary Tree Level Order Traversal](https://github.com/dengkliu/algorithms/blob/master/binary_tree_level_order_traversal.py)
* [Binary Tree Level Order Traversal II](https://github.com/dengkliu/algorithms/blob/master/binary_tree_level_order_traversal_ii.py)
* [Binary Tree Zigzag Level Order Traversal](https://github.com/dengkliu/algorithms/blob/master/binary_tree_zig_zag_level_order_traversal.py)
* [Binary Tree Vertical Order Traversal](https://github.com/dengkliu/algorithms/blob/master/binary_tree_vertical_order_traversal.py)
* [Binary Tree Vertical Order Traversal - Sorted Within Row](https://github.com/dengkliu/algorithms/blob/master/vertical_order_traversal_of_a_binary_tree.py)
* [Binary Tree Right Side View](https://github.com/dengkliu/algorithms/blob/master/binary_tree_right_side_view.py)
* [Average of Levels in Binary Tree](https://github.com/dengkliu/algorithms/blob/master/average_of_levels_in_binary_tree.py)
* [Maximum Level Sum of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/maximum_level_sum_of_a_binary_tree.py)
* [Find Largest Value in Each Tree Row](https://github.com/dengkliu/algorithms/blob/master/binary_tree_find_largest_value_in_each_tree_row.py)
* [Populating Next Right Pointers in Each Node](https://github.com/dengkliu/algorithms/blob/master/populating_next_right_pointers_in_each_node.py)
* [Minimum Height Trees](https://github.com/dengkliu/algorithms/blob/master/minimum_height_trees.py)
* [Complete Binary Tree Insert](https://github.com/dengkliu/algorithms/blob/master/complete_binary_tree_insert.py)
* [Check Completeness of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/check_completeness_of_a_binary_tree.py)

### 1.2 Divide & Conquer
* [Invert Binary Tree](https://github.com/dengkliu/algorithms/blob/master/invert_binary_tree.py)
* [Symmetric Tree](https://github.com/dengkliu/algorithms/blob/master/symmetric_tree.py)
* [Merge Two Binary Trees](https://github.com/dengkliu/algorithms/blob/master/merge_two_binary_trees.py)
* [Reverse Odd Levels of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/reverse_odd_levels_binary_tree.py)
* [Binary Tree All Paths to Leaves](https://github.com/dengkliu/algorithms/blob/master/binary_tree_paths.py)
* [Validate Binary Search Tree](https://github.com/dengkliu/algorithms/blob/master/validate_binary_search_tree.py)
* [Lowest Common Ancestor of a Binary Tree](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor.py)
* [Lowest Common Ancestor of a Binary Tree II](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_ii.py)
* [Lowest Common Ancestor of a Binary Tree III](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_iii.py)
* [Lowest Common Ancestor of a Binary Tree IV](https://github.com/dengkliu/algorithms/blob/master/binary_tree_lowest_common_ancestor_iv.py)
* [Smallest Subtree with All the Deepest Nodes](https://github.com/dengkliu/algorithms/blob/master/smallest_subtree_with_all_the_deepest_nodes.py)
* [Construct String with Parenthesis from Binary Tree](https://github.com/dengkliu/algorithms/blob/master/construct_string_from_binary_tree.py)
* [Construct Binary Tree from String with Parenthesis](https://github.com/dengkliu/algorithms/blob/master/construct_binary_tree_from_string.py)
* [Delete Nodes and Return Forest](https://github.com/dengkliu/algorithms/blob/master/delete_nodes_and_return_forest.py)
* [Delete Node in a BST](https://github.com/dengkliu/algorithms/blob/master/delete_node_in_a_bst.py)
* [Delete Subtree that Sum to 0](https://github.com/dengkliu/algorithms/blob/master/delete_tree_nodes.py)
* [Count Nodes Equals to Average of Subtree](https://github.com/dengkliu/algorithms/blob/master/count_nodes_equals_to_average_of_subtree.py)
* [Equal Tree Partition](https://github.com/dengkliu/algorithms/blob/master/equal_tree_partition.py)
* [Serialize and Deserialize Binary Tree](https://github.com/dengkliu/algorithms/blob/master/serialize_and_deserialize_binary_tree.py)
* [Serialize and Deserialize N-ary Tree](https://github.com/dengkliu/algorithms/blob/master/serialize_and_deserialize_n_ary_tree.py)
* [Binary Tree Maximum Path Sum](https://github.com/dengkliu/algorithms/blob/master/binary_tree_maximum_path_sum.py)
* [Binary Tree Path Sum Equal to Target](https://github.com/dengkliu/algorithms/blob/master/binary_tree_path_sum_equal_to_target.py)
* [Construct Binary from Preorder and Inorder Traversal](https://github.com/dengkliu/algorithms/blob/master/construct_binary_tree_from_preorder_and_inoder_traversal.py)
* [Construct Binary Search Tree from Preorder Traversal](https://github.com/dengkliu/algorithms/blob/master/construct_binary_search_tree_from_preorder_traversal.py)
* [Sum of Distances in Tree](https://github.com/dengkliu/algorithms/blob/master/sum_of_distances_in_tree.py)
* [Find Number of Coins to Place in Tree Nodes](https://github.com/dengkliu/algorithms/blob/master/find_number_of_coins_to_place_in_tree_nodes.py)
* [House Robber III](https://github.com/dengkliu/algorithms/blob/master/house_robber_iii.py)
* [Sum Root to Leaf Numbers](https://github.com/dengkliu/algorithms/blob/master/sum_root_to_leaf_numbers.py)
* [Undirected Graph Valid Tree](https://github.com/dengkliu/algorithms/blob/master/graph_valid_tree.py)
* [All Nodes Distance K in Binary Tree](https://github.com/dengkliu/algorithms/blob/master/all_nodes_distance_k_in_binary_tree.py)

#### 1.2.1 Tree's Height
* [Minimum Depth of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/minimum_depth_of_binary_tree.py)
* [Balanced Binary Tree](https://github.com/dengkliu/algorithms/blob/master/balanced_binary_tree.py)
* [Diameter of Binary Tree](https://github.com/dengkliu/algorithms/blob/master/DiameterOfBinaryTree.java)
* [Diameter of N-ary Tree](https://github.com/dengkliu/algorithms/blob/master/diameter_of_n_ary_tree.py)
* [Diameter of Undirected Tree](https://github.com/dengkliu/algorithms/blob/master/undirected_tree_diameter.py)
* [Diameter of Undirected Tree with Edge Distances](https://github.com/dengkliu/algorithms/blob/master/diameter_of_n_ary_tree_with_edge_distances.py)
* [Longest Univalue Path in Binary Tree](https://github.com/dengkliu/algorithms/blob/master/longest_univalue_path_in_binary_tree.py)
* [Number of Good Leaf Nodes Pairs](https://github.com/dengkliu/algorithms/blob/master/num_of_good_leaf_nodes_pairs.py)
* [Find leaves of binary tree](https://github.com/dengkliu/algorithms/blob/master/find_leaves_of_binary_tree.py)
* [Height of Binary Tree after Subtree Removal Queries](https://github.com/dengkliu/algorithms/blob/master/height_of_binary_tree_after_subtree_removal_queries.py)
* [Print Binary Tree](https://github.com/dengkliu/algorithms/blob/master/print_binary_tree.py)

### 1.3 Union Find 
[Union Find](https://github.com/dengkliu/algorithms/blob/master/union_find.py) is used to solve connection problem for **undirected graph**, especially for dynamic data stream (online algorithm). BFS can only be used to solve connection problem for static data (therefore BFS is offline algorithm), for data stream, the time complexity will be horrible.

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
  * [Redundant Connection](https://github.com/dengkliu/algorithms/blob/master/redundant_connection.py)
  * [Redundant Connection II](https://github.com/dengkliu/algorithms/blob/master/redundant_connection_ii.py)
  * [Graph Validate Tree I](https://github.com/dengkliu/algorithms/blob/master/graphy_valid_tree.py)
  * [Graph Validate Tree II](https://github.com/dengkliu/algorithms/blob/master/graph_valid_tree_II.py)
  * [Set Union](https://github.com/dengkliu/algorithms/blob/master/set_union.py)
  * [Accounts Merge](https://github.com/dengkliu/algorithms/blob/master/accounts_merge.py)
  * [Maximum Connected Area](https://github.com/dengkliu/algorithms/blob/master/MaximumConnectedArea.java)
  * [Maximum Association Set](https://github.com/dengkliu/algorithms/blob/master/maximum_association_set.py)
  * [Number of Islands II](https://github.com/dengkliu/algorithms/blob/master/number_of_islands_II.py)
  * [Bricks Falling When Hit](https://github.com/dengkliu/algorithms/blob/master/bricks_falling_when_hit.py)
  * [Evaluate Division](https://github.com/dengkliu/algorithms/blob/master/evaluate_division.py)
  * [Make a Large Island](https://github.com/dengkliu/algorithms/blob/master/make_a_large_island.py)

### 1.4 Trie
[Trie](https://github.com/dengkliu/algorithms/blob/master/implement_trie.py) is used to store strings while compressing the string common prefix. Its internal structure is a tree. The more common prefixes shared by the words in the dictionary, the more time saved. Trie is tested with problems including: (1) Check if a prefix or word exists in Trie (2) DFS on a Trie (3) Optimize other algorithms with Trie. The structure of Trie: (1) The character is stored on edges (2) The word is stored on nodes. The more common prefixes in the trie, the more optimization we achieve. Every time we add a word, or search a word, the best time complexity is O(L), where L is the length of the word (search in dictionary is O(1)). The worst case (no word share any prefix), we still need to traverse the entire tree.

Related coding questions
* [Add and Search Word - Data structure design](https://github.com/dengkliu/algorithms/blob/master/add_and_search_word_data_structure_design.py)
* [Identifying Strings](https://github.com/dengkliu/algorithms/blob/master/IdentifyingStrings.java)
* [Letter Combination of a Phone Number II](https://github.com/dengkliu/algorithms/blob/master/letter_combinations_of_a_phone_number.py)
* [Max Distance](https://github.com/dengkliu/algorithms/blob/master/max_distance.py)
* [Word Search II](https://github.com/dengkliu/algorithms/blob/master/word_search_II.py)
* [Word Search III](https://github.com/dengkliu/algorithms/blob/master/word_search_III.py)
  
## 2. Breath-First Search

[BFS Template](https://github.com/dengkliu/algorithms/blob/master/breadth_first_search.py)

### 2.1 Connectivity

* [Island Perimeter](https://github.com/dengkliu/algorithms/blob/master/island_perimeter.py)
* [Number of Islands](https://github.com/dengkliu/algorithms/blob/master/number_of_islands.py)
* [Number of Big Islands](https://github.com/dengkliu/algorithms/blob/master/NumberOfBigIslands.java)
* [Lake Escape](https://github.com/dengkliu/algorithms/blob/master/LakeEscape.java)
* [Validate Binary Tree Nodes](https://github.com/dengkliu/algorithms/blob/master/validate_binary_tree_nodes.py)
* [Pacific Altlantic Water Flow](https://github.com/dengkliu/algorithms/blob/master/pacific_atlantic_water_flow.py)
* [Water and Jug Problem](https://github.com/dengkliu/algorithms/blob/master/water_and_jug_problem.py)
* [Detonate the maximum bombs](https://github.com/dengkliu/algorithms/blob/master/detonate_the_maximum_bombs.py)

### 2.2 Get Shortest Path

BSF can be used to get shortest path in a simple graph. What is a simple graph? A graph is simple if 
* The edges have no direction.
* There are no weights on edges. 
* There can be at most 1 edge between 2 nodes.
* One node can not have an edge to itself. (No graph loop)

BSF can be enhanced to Shortest Path Fatser Algorithm (SPFA) to get shortest path in a complex graph. In a simple graph, the shortest path to a node is simply the number of levels that it take to reach this node. In a complex graph, you may find a node with shorter distance but appears to be in deeper level.

How does SPFA solve this problem? If we find a node in level 3 that has been visited in level 2 but now we find a shorter distance, then we throw this node back to  the queue.

* [Shortest Path to Get Food](https://github.com/dengkliu/algorithms/blob/master/shortest_path_to_get_food.py)
* [Network Delay Time](https://github.com/dengkliu/algorithms/blob/master/network_delay_time.py)
* [Path with Minimum Efforts](https://github.com/dengkliu/algorithms/blob/master/path_with_minimum_effort.py)
* [Build Post Office II](https://github.com/dengkliu/algorithms/blob/master/build_post_office.py) 
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* [The Maze](https://github.com/dengkliu/algorithms/blob/master/the_maze.py)
* [The Maze II](https://github.com/dengkliu/algorithms/blob/master/the_maze_ii.py)
* [The Maze III](https://github.com/dengkliu/algorithms/blob/master/the_maze_iii.py) 
* [Sliding Puzzle](https://github.com/dengkliu/algorithms/blob/master/sliding_puzzle.py) 
* [Sliding Puzzle II](https://github.com/dengkliu/algorithms/blob/master/SlidingPuzzleII.java) 
* [Zombie In Matrix](https://github.com/dengkliu/algorithms/blob/master/ZombieInMatrix.java)
* [Shortest Path Visiting All Nodes](https://github.com/dengkliu/algorithms/blob/master/ShortestPathVisitingAllNodes.java)
* [Word Ladder with Shortest Transformation Steps](https://github.com/dengkliu/algorithms/blob/master/word_ladder_shortest_transform_num.py)
* [Distance to nearest 0 in 01 matrix](https://github.com/dengkliu/algorithms/blob/master/01_matrix.py)

### 2.3 Get Topological Order

[Introduction](https://www.jianshu.com/p/b59db381561a) to topological order. For each node it has in-degree and out-degree. A node can be starting node if its in-degree is 0. After BFS, if the sequence length is equal to the total number of nodes, then there exists topological order for the graph. Only DAG (Directed Acyclic Graph) has topological order. 

BSF can be used to 1. find any topological order, 2. verify if there exists an topological order, 3. find the least topogical order in dictionary 4. find whether there exists just 1 topogical order.

* [Topological Sorting](https://github.com/dengkliu/algorithms/blob/master/topological_sorting.py) 
* [Course Schedule](https://github.com/dengkliu/algorithms/blob/master/course_schedule.py)
* [Course Schedule II](https://github.com/dengkliu/algorithms/blob/master/course_schedule_ii.py)
* [Alien Dictionary](https://github.com/dengkliu/algorithms/blob/master/alien_dictionary.py)

### 2.4 Others

You can also use BFS to 1. work on a 2D matrix problem regarding some maximum/minimum problems. Sometimes the problem can also be solved with DP. 2. find farthest node from a start, and furthermore find the two farthest nodes in a graph.

* [Map Jump](https://github.com/dengkliu/algorithms/blob/master/MapJump.java)
* [Longest path on a tree](https://github.com/dengkliu/algorithms/blob/master/LongestPathOnTheTree.py)
* [Second Diameter](https://github.com/dengkliu/algorithms/blob/master/second_diameter.py)

## 3. Depth-First Search

What is DFS for a graph? Start from a node, choose a neighbor and move on, until the end (no more child), if you reach the end, move back one step, and switch to another neigbor for current node, until you exhuast all the neigbors, the move back one more step and repeat. Keep searching for the target in this process, for one path you cannot revisit a node, but you can revisit the same node in a different path. 

DFS is often used to (1) solve tree problems using divide and conquer, (2) to get all solutions to meet certain requirements, and (3) to solve combination & permutation/arrangement problems. 

For (2) and (3), a technique called **backtracking** is often used. Backtracking involves DFS but with the additional strategy of pruning branches that violate constraints or cannot lead to a solution. It is a systematic method for solving problems by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the number of steps taken to reach that level.

### 3.1 Tree Traversal (Divide and Conquer) and similar problems

Find tree's problems [above](https://github.com/dengkliu/algorithms/blob/master/README.md#12-tree-divide--conquer-depth-first-search).
* [Flatten Nested List Iterator](https://github.com/dengkliu/algorithms/blob/master/flatten_nested_list_iterator.py)
* [Nested List Weight Sum](https://github.com/dengkliu/algorithms/blob/master/nested_list_weight_sum.py)
* [Clone Graph](https://github.com/dengkliu/algorithms/blob/master/clone_graph.py)

### 3.2 Find Solutions 

Find whether a solution exists or not; find a specific solution; find all solutions.

* [Generate Parentheses](https://github.com/dengkliu/algorithms/blob/master/generate_parentheses.py)
* [Couse Schedule IV](https://github.com/dengkliu/algorithms/blob/master/CourseScheduleIV.java)
* [Word Search](https://github.com/dengkliu/algorithms/blob/master/word_search.py)
* [Word Search II](https://github.com/dengkliu/algorithms/blob/master/word_search_II.py)
* [Longest Increasing Sequence in 2D Matrix](https://github.com/dengkliu/algorithms/blob/master/longest_increasing_path_in_a_matrix.py)
* [Word Break](https://github.com/dengkliu/algorithms/blob/master/word_break.py)
* [Word Break II](https://github.com/dengkliu/algorithms/blob/master/word_break_ii.py)
* [Valid Palindrome III](https://github.com/dengkliu/algorithms/blob/master/valid_palindrome_iii.py)
* [Stickers to Spell Word](https://github.com/dengkliu/algorithms/blob/master/stickers_to_spell_word.py)

### 3.3 Combination & Permutation

Find all combinations and permutations that meet a certain requirement. Find one combination and permutation that meets a certain requirement. Find the optimal combination and permutation.

* [Combination Sum](https://github.com/dengkliu/algorithms/blob/master/combination_sum.py)
* [Combination Sum II](https://github.com/dengkliu/algorithms/blob/master/combination_sum_ii.py)
* [K Sum](https://github.com/dengkliu/algorithms/blob/master/KSum.java)
* [K Sum II](https://github.com/dengkliu/algorithms/blob/master/KSumII.java)
* [Word Squares](https://github.com/dengkliu/algorithms/blob/master/word_squares.py)
* [Factorization](https://github.com/dengkliu/algorithms/blob/master/factorization.py)
* [Subsets II](https://github.com/dengkliu/algorithms/blob/master/subset_II.py)

## 4. Dynamic Programming

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection
of **simpler subproblems**, solving each of those subproblems **just once**, and **storing their solutions** 
using a memory-based data structure(array, map, etc). 

Trade the space complexity for time complexity.

### 4.1 Coordinate DP
* [Modern Ludo I](https://github.com/dengkliu/algorithms/blob/master/ModernLudoI.java)
* [Climbing Stairs](https://github.com/dengkliu/algorithms/blob/master/climbing_stairs.py)
* [Number of Ways to Stay in the Same Place After Some Steps](https://github.com/dengkliu/algorithms/blob/master/number_of_ways_to_stay_in_same_place_after_some_steps.py)
* [Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/)
* [Minimum Falling Path Sum](https://github.com/dengkliu/algorithms/blob/master/minimum_failing_path_sum.py)
* [Calculate the Sum of Path](https://github.com/dengkliu/algorithms/blob/master/calculate_the_sum_of_path.py)
* [Push Dominoes](https://github.com/dengkliu/algorithms/blob/master/push_dominoes.py)
* https://leetcode.com/problems/distinct-subsequences/description/
* [Distinct Subsequences II](https://github.com/dengkliu/algorithms/blob/master/distinct_subsequences.py)
* [Subset II](https://github.com/dengkliu/algorithms/blob/master/subset_II.py)
* [Paint House](https://github.com/dengkliu/algorithms/blob/master/paint_house.py)
* [Decode Ways](https://github.com/dengkliu/algorithms/blob/master/decode_ways.py)
* [Decode Ways II](https://github.com/dengkliu/algorithms/blob/master/decode_ways_II.py)
* [Longest Increasing Subsequence](https://github.com/dengkliu/algorithms/blob/master/longest_increasing_subsequence.py)
* https://leetcode.com/problems/longest-increasing-subsequence-ii/description/
* [Rat Jump](https://github.com/dengkliu/algorithms/blob/master/rat_jump.py)
* https://leetcode.com/problems/frog-jump/description/
* [Maximal Square](https://github.com/dengkliu/algorithms/blob/master/maximal_square.py)
* [Count Square Submatrices with All Ones](https://github.com/dengkliu/algorithms/blob/master/count_squares.py)
* [Distance to nearest 0 in 01 matrix](https://github.com/dengkliu/algorithms/blob/master/01_matrix.py)

### 4.2 Backpack DP 
* [Knapsack](https://github.com/dengkliu/algorithms/blob/master/backpack.py)
* [Backpack II](https://github.com/dengkliu/algorithms/blob/master/backpack_II.py)
* [Backpack III](https://github.com/dengkliu/algorithms/blob/master/backpack_III.py)
* [Backpack IV](https://github.com/dengkliu/algorithms/blob/master/backpack_IV.py)
* [Backpack V](https://github.com/dengkliu/algorithms/blob/master/backpack_V.py)
* [Backpack VII](https://github.com/dengkliu/algorithms/blob/master/backpack_VII.py)
* [Backpack VIII](https://github.com/dengkliu/algorithms/blob/master/backpack_VIII.py)
* [Backpack IX](https://github.com/dengkliu/algorithms/blob/master/backpack_IX.py)
* [Backpack X](https://github.com/dengkliu/algorithms/blob/master/backpack_X.py)
* [Minimum Number of Coins to Make a Change](https://github.com/dengkliu/algorithms/blob/master/minimum_number_of_coins_to_make_a_change.py)
* [Partition Equal Subset Sum](https://github.com/dengkliu/algorithms/blob/master/partition_equal_subset_sum.py)
* [Best Time to Buy and Sell Stock III](https://github.com/dengkliu/algorithms/blob/master/BestTimeToBuyAndSellStockIII.java)
* [K Sum](https://github.com/dengkliu/algorithms/blob/master/KSum.java)
* [K Sum II](https://github.com/dengkliu/algorithms/blob/master/KSumII.java)
* [Card Game](https://github.com/dengkliu/algorithms/blob/master/card_game.py)
* [Profitable Schemes](https://github.com/dengkliu/algorithms/blob/master/profitable_schemes.py)
* [Float Combination Sum](https://github.com/dengkliu/algorithms/blob/master/float_combination_sum.py)
* https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
* https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

### 4.3 Interval DP
* [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/description/)
* [Stone Game](https://github.com/dengkliu/algorithms/blob/master/stone_game.py)
* [Stone Game II](https://github.com/dengkliu/algorithms/blob/master/stone_game_II.py)
* [Minimum Cost to Merge Stones](https://github.com/dengkliu/algorithms/blob/master/minimum_cost_to_merge_stones.py)

### 4.4 Prefix DP
* [Longest Common Subsequence](https://github.com/dengkliu/algorithms/blob/master/longest_common_sequence.py)
* [Height of Binary Tree after Subtree Removal Queries](https://github.com/dengkliu/algorithms/blob/master/height_of_binary_tree_after_subtree_removal_queries.py)

## 5. Greedy

* [Best Time to Buy and Sell Stock](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock.py)
* [Best Time to Buy and Sell Stock II](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock_II.py)
* [Best Time to Buy and Sell Stock V](https://github.com/dengkliu/algorithms/blob/master/best_time_to_buy_and_sell_stock_V.py)
* [Queue Reconstruction by Height](https://github.com/dengkliu/algorithms/blob/master/queue_reconstruction_by_height.py)

## 6. Prefix Sum 前缀和
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
* [Random Pick with Weights](https://github.com/dengkliu/algorithms/blob/master/random_pick_with_weight.py)
* [Continous Subarrary Sum Divisible By K](https://github.com/dengkliu/algorithms/blob/master/continous_subarray_sum.py)

## 7. Scanning Line 扫描线

Scanning line is usuallly used to solve interval related problems. 

* [Number of Airplanes in the Sky](https://github.com/dengkliu/algorithms/blob/master/number_of_airplanes_in_the_sky.py) ✅ 解决区间问题的经典题，把起点和终点分别flag，在时间上进行排序。

## 8. Two Pointers 双指针

Two pointers are usually used when:
* Sliding window problem
* Time complexity is O(N) (80%)
* In-place algorithm, you can not use extra space.
* Subarray or substring problem (50%)
* Palindrome problem (50%)

### 8.1 [Same direction two pointers](https://github.com/dengkliu/algorithms/blob/master/same_direction_two_pointers.py) 
Two pointers start from the head of array and go to the end. 

* [Validate word abbreviation](https://github.com/dengkliu/algorithms/blob/master/valid_word_abbreviation.py)
* [Interval List Intersections](https://github.com/dengkliu/algorithms/blob/master/interval_list_intersections.py)
* [Dot Product of 2 Sparse Vector](https://github.com/dengkliu/algorithms/blob/master/dot_product_of_2_sparse_vectors.py)
* [Product of 2 Run Length Encoded Arrays](https://github.com/dengkliu/algorithms/blob/master/product_of_two_run_length_encoded_arrays.py)
* [Minimum Size Subarray Sum at Least Target](https://github.com/dengkliu/algorithms/blob/master/minimum_size_of_subarray_sum_no_less_than_target.py)
* [Substring With At Least K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/substring_with_at_least_K_distinct_characters.py) 
* [Minimum Window Substring](https://github.com/dengkliu/algorithms/blob/master/minimum_window_substring.py)
* [Longest Substring Without Repeating Characters](https://github.com/dengkliu/algorithms/blob/master/longest_substring_without_repeating_characters.py)
* [Longest Substring With At Most K Distinct Characters](https://github.com/dengkliu/algorithms/blob/master/LongestSubstringWithAtMostKDistinctCharacters.java) 
* [Subarray Sum II](https://github.com/dengkliu/algorithms/blob/master/subarray_sum_II.py)
* [Merge Two Sorted Array In Place](https://github.com/dengkliu/algorithms/blob/master/merge_sorted_array.py)

### 8.2 Fixed Size Sliding Window 固定长度滑动窗口

* [Grumpy Bookstore Owner](https://github.com/dengkliu/algorithms/blob/master/GrumpyBookStoreOwner.java) ✅ Slding window经典题，枚举终点，注意第一个初始状态window的位置，初始化的时候直接assume window在这个位置，求得一个解，然后移动window，打擂台。
* [Pick Apples](https://github.com/dengkliu/algorithms/blob/master/PickApples.java) ✅ 典型的fixed size sliding window + 双字段问题。注意双字段问题可以用隔板法，隔板法用for loop,隔板位置从0到n-1，[0, i) [i, n-1], 在子函数里 start - end <= 0 或者 window size直接返回-1.

### 8.3 Opposite direction two pointers
* [Two Sim VII](https://github.com/dengkliu/algorithms/blob/master/TwoSumVII.java)
* [2 Sum - Sorted List](https://github.com/dengkliu/algorithms/blob/master/two_sum_ii.py)
* [3 Sum Smaller](https://github.com/dengkliu/algorithms/blob/master/3sum_smaller.py)
* [3 Sum Closest](https://github.com/dengkliu/algorithms/blob/master/3_sum_closest.py)
* [4 Sum](https://github.com/dengkliu/algorithms/blob/master/4_sum.py)
* [Valid Palindrome II](https://github.com/dengkliu/algorithms/blob/master/valid_palindrome_ii.py)
  
### Back direction two pointers
* [Shortest Palindrome](https://github.com/dengkliu/algorithms/blob/master/ShortestPalindrome.java) 

## 9. Binary Search 二分查询

You may want to use binary search when -
* When the interviewer ask you to find a solution that is better than O(N)
* Find a cut in the array, which makes the left half meet the condition, the other half don't.
* The array is sorted, find a global maximum or minimum value to meet a certain requirement
* Find a local minimum or maximum.

Related coding problem -

* [Maximum Number in Mountain Sequence](https://github.com/dengkliu/algorithms/blob/master/maximum_number_in_mountain_sequence.py)
* [Find Peak Element](https://github.com/dengkliu/algorithms/blob/master/find_peak_element.py)
* [Find Peak Element II](https://github.com/dengkliu/algorithms/blob/master/find_peak_element_II.py)
* [Find in Mountain Array](https://github.com/dengkliu/algorithms/blob/master/find_in_mountain_array.py)
* [H-Index II](https://github.com/dengkliu/algorithms/blob/master/h_index_ii.py)
* [Find word](https://github.com/dengkliu/algorithms/blob/master/find_words.py) 
* [Search in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/search_in_rotated_sorted_array.py)
* [Find Minimum in Rotated Sorted Array](https://github.com/dengkliu/algorithms/blob/master/find_minimum_in_rotated_sorted_array.py)
* [Wood Cut](https://github.com/dengkliu/algorithms/blob/master/wood_cut.py)
* [Copy Books](https://github.com/dengkliu/algorithms/blob/master/copy_books.py) 
* [Find K Closet Elements](https://github.com/dengkliu/algorithms/blob/master/find_k_closet_elements.py) 
* [Heaters](https://github.com/dengkliu/algorithms/blob/master/heaters.py)
* [Median of Two Sorted Array](https://github.com/dengkliu/algorithms/blob/master/median_of_two_sorted_arrays.py)
* [Maximum Average Subarray II](https://github.com/dengkliu/algorithms/blob/master/MaximumAverageSubarrayII.java) 
* [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)
* [Random Pick with Weights](https://github.com/dengkliu/algorithms/blob/master/random_pick_with_weight.py)
* [Pow(x, n)](https://github.com/dengkliu/algorithms/blob/master/powx_n.py)

## 10. Sorting
* [Quick sort](https://github.com/dengkliu/algorithms/blob/master/quick_sort.py)
* [Merge sort](https://github.com/dengkliu/algorithms/blob/master/merge_sort.py)
* [Count of Smaller Numbers After Self](https://github.com/dengkliu/algorithms/blob/master/count_of_smaller_numbers_after_itself.py)

## 11. Useful data structures
### 11.1. Monotonic Stack/Queue
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
* [Buildings With an Ocean View](https://github.com/dengkliu/algorithms/blob/master/buildings_with_an_ocean_view.py)

### 12.2 Segment Tree
Here is the [implementation](https://github.com/dengkliu/algorithms/blob/master/segment_tree.py) of segment tree. For an array of size N, a practical upper estimate for the size of a segment tree array is about 4 * N, which safely covers the cases where 
N is not a power of two, ensuring there is enough space in the array to represent the tree. 
* If N = 8, the size of the segment tree is 15 nodes (2 * N - 1).
* If N = 10(not a power of two), the next power of two is 16 The full size of the segment tree can be up to 2 × 16 − 1 = 31 nodes. Using the practical estimate, allocating space for 40 nodes is safe and simple.

### 12.3 Linked List
* [Reverse Linked List](https://github.com/dengkliu/algorithms/blob/master/reverse_singly_linked_list.py)
* [Insert into a Sorted Circular Linked List](https://github.com/dengkliu/algorithms/blob/master/insert_into_a_sorted_circular_linked_list.py)
* [LRU Cache](https://github.com/dengkliu/algorithms/blob/master/lru_cache.py)
* [Merge Two Sorted Linked Lists](https://github.com/dengkliu/algorithms/blob/master/merge_two_sorted_list.py)
* [Merge K Sorted Linked Lists](https://github.com/dengkliu/algorithms/blob/master/merge_k_sorted_list.py)

### 12.4 Stack
* [Minimum Remove to Make Valid Parentheses](https://github.com/dengkliu/algorithms/blob/master/minimum_remove_to_make_valid_parentheses.py)
* [Min Stack](https://github.com/dengkliu/algorithms/blob/master/min_stack.py)
* [Basic calculator](https://github.com/dengkliu/algorithms/blob/master/basic_calculator.py)
* [Basic calculator II](https://github.com/dengkliu/algorithms/blob/master/basic_calculator_ii.py)
* [Basic calculator III](https://github.com/dengkliu/algorithms/blob/master/basic_calculator_iii.py)
* [Simplify Path](https://github.com/dengkliu/algorithms/blob/master/simplify_path.py)

### 12.4 FIFO queue
* [Move Average from Data Stream](https://github.com/dengkliu/algorithms/blob/master/move_average_from_data_stream.py)

### 12.5 Heap (Priority Queue)
In Python, you need to import heapq library, and use heapq.heappop(heap) and heap.heappush(heap, element) to do pop and push operation.
* [Minimum Cost to Hire_K_Workers](https://github.com/dengkliu/algorithms/blob/master/minimum_cost_to_hire_K_workers.py)
* [Kth largest element in an array](https://github.com/dengkliu/algorithms/blob/master/kth_largest_element_in_an_array.py)
* [K Closest Points to Origin](https://github.com/dengkliu/algorithms/blob/master/k_closest_points_to_origin.py)

### 12.6 Dictionary
Use python dictionary to achieve O(1) search time.
* [2 Sum](https://github.com/dengkliu/algorithms/blob/master/two_sum.py)
* [Custom Sort String](https://github.com/dengkliu/algorithms/blob/master/custom_sort_string.py)
* [Group Shifted String](https://github.com/dengkliu/algorithms/blob/master/group_shifted_strings.py)
* [Maximum Swap](https://github.com/dengkliu/algorithms/blob/master/maximum_swap.py)

## 13. String, Math, and Others
These are other problems related to plain string or mathematical problems.
* [Nth Digit](https://github.com/dengkliu/algorithms/blob/master/nth_digit.py)
* [Valid Palindrome](https://github.com/dengkliu/algorithms/blob/master/valid_palindrome.py)
* [Valid Number](https://github.com/dengkliu/algorithms/blob/master/valid_number.py)
* [Greatest Common Divisor String](https://github.com/dengkliu/algorithms/blob/master/greatest_common_divisor_of_strings.py)
