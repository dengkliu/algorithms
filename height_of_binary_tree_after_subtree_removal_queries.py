# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

# https://www.youtube.com/watch?v=s62a0uxeRkE

# You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

# You have to perform m independent queries on the tree where in the ith query you do the following:

# Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
# Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

# Note:

# The queries are independent, so the tree returns to its initial state after each query.
# The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        nodes = []
        nodes_depth = []
        nodes_subtree_index = {}

        def treeTraversalHelper(root, depth):
            if not root:
                return
            
            nodes.append(root.val)
            nodes_depth.append(depth)
            start_index = len(nodes) - 1
            treeTraversalHelper(root.left, depth + 1)
            treeTraversalHelper(root.right, depth + 1)
            end_index = len(nodes) - 1
            nodes_subtree_index[root.val] = (start_index, end_index)

        treeTraversalHelper(root, 0)

       
        max_depth_l_to_r = [0 for _ in range(len(nodes_depth))]
        max_depth_r_to_l = [0 for _ in range(len(nodes_depth))]
        max_depth_l = 0
        max_depth_r = 0 

        for i in range(len(nodes_depth)):
            max_depth_l = max(max_depth_l, nodes_depth[i])
            max_depth_l_to_r[i] = max_depth_l

            max_depth_r = max(max_depth_r, nodes_depth[len(nodes_depth) - 1 - i])
             # Use array instead of list because inserting into the 0 index of python list is very inefficient 
            max_depth_r_to_l[len(nodes_depth) - 1 - i] = max_depth_r

        result = []

        for query in queries:
            l_index, r_index = nodes_subtree_index[query]
            max_depth_l = 0 if l_index == 0 else max_depth_l_to_r[l_index - 1]
            max_depth_r = 0 if r_index == len(nodes_depth) - 1 else max_depth_r_to_l[r_index + 1]

            result.append(max(max_depth_l, max_depth_r))

        return result