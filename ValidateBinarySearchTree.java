
// https://www.lintcode.com/problem/95/
// Given a binary tree, determine if it is a valid binary search tree (BST).

// Assume a BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
// A single node tree is a BST

// Divide and conquer.
// A tree is valid BST only if its left child and right child is valid BST 
// And the all left children is smaller than it and all right children is greater than it.
// A top down solution

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

public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {

        if (root == null) {
            return true;
        }

        int max = Integer.MAX_VALUE;
        int min = Integer.MIN_VALUE;

        TreeNode left = root.left;
        TreeNode right = root.right;

        return isValid(root.left, min, root.val) 
            && isValid(root.right, root.val, max);
    }

    boolean isValid(TreeNode root, int lowerBound, int upperBound) {

        if (root == null) {
            return true;
        }

        // when the lower and upper bound is Integer max and min, there is actually no bound
        boolean isHigherThanLowerBound = root.val > lowerBound 
            || lowerBound == Integer.MIN_VALUE;

        boolean isLessThanUpperBound = root.val < upperBound 
            || upperBound == Integer.MAX_VALUE;

        if (isHigherThanLowerBound && isLessThanUpperBound) {
            return isValid(root.left, lowerBound, root.val) 
                && isValid(root.right, root.val, upperBound);
        }

        return false;
    }
}
