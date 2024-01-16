https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result = []

        self.postorder(root, result)

        return result

    def postorder(self, root, result):
        if root.left:
            self.postorder(root.left, result)
        if root.right:
            self.postorder(root.right, result)
        result.append(root.val)
