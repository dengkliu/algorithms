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

    min_column = float("inf")
    max_column = float("-inf")

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        col_to_node = {} 
        node_to_col = {}
        node_to_col[root] = 0

        queue = collections.deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            col = node_to_col[cur]

            self.min_column = min(self.min_column, col)
            self.max_column = max(self.max_column, col)

            if col not in col_to_node:
                col_to_node[col] = []
            col_to_node[col].append(cur.val)

            if cur.left:
                queue.append(cur.left)
                node_to_col[cur.left] = col - 1
            if cur.right:
                queue.append(cur.right)
                node_to_col[cur.right] = col + 1
                
        result = []

        for i in range(self.min_column, self.max_column + 1):
            result.append(col_to_node[i])

        return result
