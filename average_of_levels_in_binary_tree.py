# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if not root:
            return result
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            # why do we want to define it as a float?
            total_val = 0.0
            for i in range(size):
                node = queue.popleft()
                total_val += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(total_val/size)
        
        return result
        