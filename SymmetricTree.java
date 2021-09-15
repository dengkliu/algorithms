// https://www.lintcode.com/problem/1360
// Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

// Input: {1,2,2,3,4,4,3}
// Output: true
// Explanation:
//    1
//   / \
//  2   2
// / \ / \
//3  4 4  3
//This binary tree {1,2,2,3,4,4,3} is symmetric


//       1
//      / \
//     2   2
//    / \ / \
//   3  4 4  3
//  / \     / \
// 5   7   7   5
// 1. 典型的分治法
// 一个树是对称 == root的左右子节点相等 以及左子树的右子树 和 右子树的左子树 相等 如此类推

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
     * @param root: root of the given tree
     * @return: whether it is a mirror of itself 
     */
    public boolean isSymmetric(TreeNode root) {

        if (root == null) {
            return true;
        }

        return isSymmetricTree(root.left, root.right);

    }

    boolean isSymmetricTree(TreeNode root1, TreeNode root2) {

        if (root1 == null && root2 == null) {
            return true;
        }

        if (root1 == null || root2 == null) {
            return false;
        }

        if (root1.val != root2.val) {
            return false;
        }

        return isSymmetricTree(root1.right, root2.left) 
            && isSymmetricTree(root1.left, root2.right);
    }
}

// 2. 假如一个树是对称的，那么在中序遍历和前序遍历里 把左和右对调之后 是不影响结果的