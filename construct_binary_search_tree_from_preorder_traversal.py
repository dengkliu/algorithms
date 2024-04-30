# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or preorder == []:
            return None
        
        # why do we first need to copy and then sort?
        inorder = list(preorder)
        inorder.sort()

        # [8, 5, 1, 7, 10, 12]
        # [1, 5, 7, 8, 10, 12]
        def buildTreeHelper(preorder, pre_l, pre_r, inorder, in_l, in_r):
            if pre_l > pre_r:
                return None
            
            root = TreeNode(preorder[pre_l])
            
            if pre_l == pre_r:
                return root

            root_index = inorder.index(root.val)
            num_nodes_l = root_index - in_l

            root.left = buildTreeHelper(preorder, pre_l + 1, pre_l + num_nodes_l, inorder, in_l, root_index - 1)
            root.right = buildTreeHelper(preorder, pre_l + num_nodes_l + 1, pre_r, inorder, root_index + 1, in_r)

            return root

        return buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)