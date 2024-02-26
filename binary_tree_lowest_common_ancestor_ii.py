# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/

# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
# If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". 
# A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # This is basically a bottom up approach
        def lca(root, p, q):
            if root is None:
                return (None, 0)

            l, l_count = lca(root.left, p, q)
            r, r_count = lca(root.right, p, q)

            if root == p or root == q:
                return (root, 1 + l_count + r_count)
            
            if l and r:
                return (root, 2)

            if l:
                return (l, l_count)
            else:
                return (r, r_count)
        
        node, count = lca(root, p, q)

        return node if count == 2 else None
