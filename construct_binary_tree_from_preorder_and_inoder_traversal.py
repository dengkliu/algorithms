# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or len(preorder) == 0:
            return None

        def buildTreeHelper(preorder, pre_l, pre_r, inorder, in_l, in_r):

            if pre_l > pre_r:
                return None
            
            # Get the current subtree root, always the leftmost element in preorder
            cur_root = TreeNode(preorder[pre_l], None, None)

            if pre_l == pre_r:
                return cur_root
        
            # Find the index of this root in inorder
            root_index = inorder.index(cur_root.val)

            # how many nodes in the left subtree of this root
            num_nodes_l = root_index - in_l 

            # how many nodes in the right subtree of this root
            num_nodes_r = in_r - root_index

            # the left subtree range in preorder: pre_l + 1 to pre_l + num_nodes_l
            # the left subtree range in inorder: in_l, in_index - 1
            cur_root.left = buildTreeHelper(preorder, pre_l + 1, pre_l + num_nodes_l, inorder, in_l, root_index - 1)

            # the right subtree range in preorder: pre_l + num_nodes_l to pre_r
            # the right subtree range in inoder: root_index + 1, in_r
            cur_root.right = buildTreeHelper(preorder, pre_l + num_nodes_l + 1, pre_r, inorder, root_index + 1, in_r)

            return cur_root

        return buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)