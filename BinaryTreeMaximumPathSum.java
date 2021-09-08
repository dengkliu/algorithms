// https://www.lintcode.com/problem/94

// Given a binary tree, find the maximum path sum.
// The path may start and end at any node in the tree.
// (Path sum is the sum of the weights of nodes on the path between two nodes.

// Input:
// tree = {1,2,3}
// Output:
// 6

// Divide and conquer
// For each node, the maximum path is 
// 1) the solution on its left subtree
// 2) the solution on its right subtree
// 3) the maximum path ending at its left child + the maximum path ending at its right child + its value
// There can be negative sum, always compare with 0

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
     * @return: An integer
     */
    public int maxPathSum(TreeNode root) {
        // write your code here
        int[] result = new int[1];

        result[0] = Integer.MIN_VALUE;

        if (root == null) {
            return 0;
        }

        int maxLeftPath = helper(root.left, result);
        int maxRightPath = helper(root.right, result);

        return Math.max(result[0], 
            Math.max(0, maxLeftPath) + Math.max(0, maxRightPath) + root.val);
    }

    int helper(TreeNode root, int[] result) {

        if (root == null) {
            return 0;
        }

        int maxLeftPath = helper(root.left, result);
        int maxRightPath = helper(root.right, result);

        result[0] = Math.max(result[0], 
            Math.max(0, maxLeftPath) + Math.max(0, maxRightPath) + root.val);

        return Math.max(0, Math.max(maxLeftPath, maxRightPath)) + root.val;
    }

}