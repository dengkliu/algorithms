// https://www.lintcode.com/problem/1181
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

public class Solution {

    int diameter = 0;
    
    /**
     * @param root: a root of binary tree
     * @return: return a integer
     */
    public int diameterOfBinaryTree(TreeNode root) {

        if (root == null) {
            return diameter;
        }

        dfs(root);

        return diameter;
    }

    int dfs(TreeNode node) {

        if (node == null) {
            return -1;
        }

        int pathLenRight = dfs(node.right);
        int pathLenLeft = dfs(node.left);

        int pathLenRoot = Math.max(pathLenLeft, pathLenRight) + 1;

        diameter = Math.max(diameter, pathLenRight + pathLenLeft + 2);

        return pathLenRoot;
    }
}