# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = collections.deque()
        queue.append(root)

        result = []

        while queue:
            size = len(queue)
            max_val = -float('inf')
            
            for i in range(size):
                cur = queue.popleft()
                max_val = max(max_val, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            result.append(max_val)

        return result