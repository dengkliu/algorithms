# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        level = 0
        result = []
        while queue:
            curr_level_nodes = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if level % 2 == 0:
                    curr_level_nodes.append(node.val)
                else:
                    curr_level_nodes.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_level_nodes)
            level += 1
        
        return result