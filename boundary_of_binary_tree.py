# https://leetcode.com/problems/boundary-of-binary-tree/description/

# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

# Left Boundary:
# All nodes in the boundary are non-leaf nodes
# If the node has a left child, that left child would be in the left boundary UNLESS it is a leaf node
# If the node does NOT have a left child but does have a right child, that right child would be in the left boundary UNLESS it is a leaf node
# Right Boundary:
# All nodes in the boundary are non-leaf nodes
# If the node has a right child, that right child would be in the right boundary UNLESS it is a leaf node
# If the node does NOT have a right child but does have a left child, that left child would be in the right boundary UNLESS it is a leaf node

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ROOT = 1
        LEFT_BOUNDARY = 2
        RIGHT_BOUNDARY = 3
        MIDDLE = 4

        root_boundary = []
        left_boundary = []
        right_boundary = []
        leaves = []

        def dfs(root, node_type):
            if not root:
                return

            if node_type == ROOT:
                root_boundary.append(root.val)
                dfs(root.left, LEFT_BOUNDARY)
                dfs(root.right, RIGHT_BOUNDARY)

            if node_type == LEFT_BOUNDARY:
                #  Why do we check leaves first?
                if not root.right and not root.left:
                    leaves.append(root.val)
                else:
                    left_boundary.append(root.val)
                    
                if root.left:   
                    dfs(root.left, LEFT_BOUNDARY)
                    dfs(root.right, MIDDLE)
                else:
                    dfs(root.right, LEFT_BOUNDARY)

            if node_type == MIDDLE:
                if not root.right and not root.left:
                    leaves.append(root.val)
                dfs(root.left, MIDDLE)
                dfs(root.right, MIDDLE)
            
            if node_type == RIGHT_BOUNDARY:
                if not root.right and not root.left:
                    leaves.append(root.val)
                else:
                    right_boundary.insert(0, root.val)
                
                if not root.right:
                    dfs(root.left, RIGHT_BOUNDARY)
                else:
                    dfs(root.left, MIDDLE)
                    dfs(root.right, RIGHT_BOUNDARY)

        dfs(root, ROOT)

        return root_boundary + left_boundary + leaves + right_boundary