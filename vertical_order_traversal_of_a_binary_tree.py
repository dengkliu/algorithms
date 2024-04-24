# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
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
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur, col = queue.popleft()
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                
                nodes_in_col = col_to_node.get(col, [])
                nodes_in_col.append((cur.val, level))
                col_to_node[col] = nodes_in_col
                if cur.left:
                    queue.append((cur.left, col -1))
                if cur.right:
                    queue.append((cur.right, col + 1))
            level += 1    
        result = []

        for i in range(min_column, max_column + 1):
            nodes = col_to_node[i]
            nodes.sort(key=lambda nodes:(nodes[1], nodes[0]))
            nodes_val = [node[0] for node in nodes]
            result.append(nodes_val)

        return result