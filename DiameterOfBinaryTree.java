// https://leetcode.com/problems/diameter-of-binary-tree/
// Given a binary tree, you need to compute the length of the diameter of the tree. 
// The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = [0]

        def diameterHelper(root):
            if not root:
                return 0

            l = diameterHelper(root.left)
            r = diameterHelper(root.right)

            l_through_root = 0
            r_through_root = 0

            if root.left:
                l_through_root = 1 + l
            if root.right:
                r_through_root = 1 + r

            result[0] = max(result[0], l_through_root + r_through_root)

            return max(l_through_root, r_through_root)

        diameterHelper(root)

        return result[0]
