// https://www.lintcode.com/problem/864
// Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees 
// which have the equal sum of values after removing exactly one edge on the original tree.

// The range of tree node value is in the range of [-100000, 100000]. --> which means the sum could be 0
// 1 <= n <= 10000
// You can assume that the tree is not null

// 典型的DFS问题 一个🌲的sum == 左子树sum + 右子树sum

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
     * @param root: a TreeNode
     * @return: return a boolean
     */
    public boolean checkEqualTree(TreeNode root) {

        if (root == null) {
            return true;
        }

        Set<Integer> sumSet = new HashSet<>();

        // 整个🌲和 = 左子树和 + 右子树和
        // To avoid the case the treeSum == 0, 0/2 itself is 0, so we don't want to
        // add the sum to the set
        int treeSum = root.val + getTreeSum(root.left, sumSet) + getTreeSum(root.right, sumSet);

        return (treeSum%2 == 0) && (sumSet.contains(treeSum/2));

    }

    int getTreeSum(TreeNode root, Set<Integer> sumSet) {

        if (root == null) {
            return 0;
        }
        
        int sum = root.val + getTreeSum(root.left, sumSet) + getTreeSum(root.right, sumSet);
        
        // 在得到这棵树的和后放入set
        sumSet.add(sum);
        
        return sum;
    }
}
