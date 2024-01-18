# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/

# Given the root of a binary tree and an array of TreeNode objects nodes, 
# return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". 
# A descendant of a node x is a node y that is on the path from node x to some leaf node.

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        if root is None or root in nodes:
            return root
        
        l = self.lowestCommonAncestor(root.left, nodes) 
        r = self.lowestCommonAncestor(root.right, nodes)

        # one node found on the left and the other found on the right
        if l and r:
            return root

        # one node found the left or right, and None found from the other side
        # can just return because the other node must be the children of this node
        return l or r

