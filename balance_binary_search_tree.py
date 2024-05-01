# https://leetcode.com/problems/balance-a-binary-search-tree/

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inOrderTraversal(root):
            if not root:
                return
            inOrderTraversal(root.left)
            in_order.append(root.val)
            inOrderTraversal(root.right)

        def dfs(in_order, l, r):
            if l > r:
                return None
            mid = (l + r)//2
            root = TreeNode(in_order[mid])
            root.left = dfs(in_order, l, mid - 1)
            root.right = dfs(in_order, mid + 1, r)
            return root

        if not root:
            return None
        
        in_order = []

        inOrderTraversal(root)

        return dfs(in_order, 0, len(in_order) - 1)