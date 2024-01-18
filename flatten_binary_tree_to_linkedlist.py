# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Flatten a binary tree to a fake "linked list" in pre-order traversal.
# Here we use the right pointer in TreeNode as the next pointer in ListNode.

# Don't forget to mark the left child of each node to null. 
# Or you will get Time Limit Exceeded or Memory Limit Exceeded.

# Input:{1,2,5,3,4,#,6}
# Output：{1,#,2,#,3,#,4,#,5,#,6}
# Explanation：
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

#1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root is None:
            return None
        
        stack = []
        result = []

        stack.append(root)

        # [1 2]
        # [5 2]
        # [5 4 3]
        while stack:
            node = stack.pop()
            result.append(node)
            if len(result) >= 2:
                prevNode = result[-2]
                prevNode.right = node
                prevNode.left = None
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result[0]
