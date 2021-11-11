# https://www.lintcode.com/problem/902/

# Given a binary search tree, write a function to find the kth smallest element in it.

# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        
        if root is None:
            return None

        stack = []
        inorder_traversal_result = []

        dummy_node = TreeNode(0)

        dummy_node.right = root

        stack.append(dummy_node)

        while stack:
            node = stack.pop()
            if node.right is not None:
                node = node.right
                stack.append(node)
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left   
            if stack:         
                inorder_traversal_result.append(stack[-1])
            if len(inorder_traversal_result) == k:
                return inorder_traversal_result[-1].val

        return None
