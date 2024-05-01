# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = collections.deque()
        queue.append(root)
        prev_right_null = False
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # 1. Why do we need this check?
                if prev_right_null and (node.right or node.left):
                    return False
                # 2. Why do we need this check?
                if not node.left and node.right:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                else:
                    prev_right_null = True
        
        return True