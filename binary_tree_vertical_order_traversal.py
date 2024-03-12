# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        min_column = float("inf")
        max_column = float("-inf")

        if root is None:
            return []
        # build this dictionary from column to node
        col_to_node = {} 

        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            cur, col = queue.popleft()

            min_column = min(min_column, col)
            max_column = max(max_column, col)

            nodes_in_col = col_to_node.get(col, [])
            nodes_in_col.append(cur.val)
            col_to_node[col] = nodes_in_col

            if cur.left:
                queue.append((cur.left, col -1))
            if cur.right:
                queue.append((cur.right, col + 1))
                
        result = []

        for i in range(min_column, max_column + 1):
            result.append(col_to_node[i])

        return result
