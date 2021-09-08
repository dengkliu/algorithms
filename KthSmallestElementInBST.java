// https://www.lintcode.com/problem/902/

// Given a binary search tree, write a function kth smallest to find the kth smallest element in it.

// You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

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
     * @param root: the given BST
     * @param k: the given k
     * @return: the kth smallest element in BST
     */
    public int kthSmallest(TreeNode root, int k) {
        // write your code here
        if (root == null) {
            return 0;
        }

        int[] result = new int[1];

        List<TreeNode> nodes = new ArrayList<>();

        inOrder(root, nodes, k, result);
        
        return result[0];
    }

    void inOrder(TreeNode root, List<TreeNode> nodes, int k, int[] result) {

        if (root == null) {
            return;
        }

        inOrder(root.left, nodes, k, result);
        nodes.add(root);
        if (nodes.size() == k) {
            result[0] = root.val;
            return;
        }
        inOrder(root.right, nodes, k, result);
    }
}

