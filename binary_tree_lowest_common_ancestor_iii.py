# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#    public int val;
#    public Node left;
#    public Node right;
#    public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to # be a descendant of itself)."

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        cur_p, cur_q = p, q

        while cur_p != cur_q:
            cur_p = cur_p.parent if cur_p.parent else q
            cur_q = cur_q.parent if cur_q.parent else p

        return cur_p
