// Flatten a binary tree to a fake "linked list" in pre-order traversal.
// Here we use the right pointer in TreeNode as the next pointer in ListNode.

// Don't forget to mark the left child of each node to null. 
// Or you will get Time Limit Exceeded or Memory Limit Exceeded.

// Input:{1,2,5,3,4,#,6}
// Output：{1,#,2,#,3,#,4,#,5,#,6}
// Explanation：
//     1
//    / \
//   2   5
//  / \   \
// 3   4   6

//1
//\
// 2
//  \
//   3
//    \
//     4
//      \
//       5
//        \
//         6

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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {

        // 一定要用一个list存放已经遍历到的节点，这在后面有用
        List<TreeNode> nodes = new ArrayList<>();

        preOrder(root, nodes);

    }

    void preOrder(TreeNode root, List<TreeNode> nodes) {

        if (root == null) {
            return;
        }

        // 前序，先把node加进来
        nodes.add(root);

        // 先cache一下root的right
        TreeNode right = root.right;

        // 处理左边
        preOrder(root.left, nodes);

        // 左边处理好了，就assign给当前node的next, 并且把当前node左边清空
        root.right = root.left;
        root.left = null;

        // 找到左边最后一个node
        TreeNode leftEnd = nodes.get(nodes.size() - 1);

        // 处理右边
        preOrder(right, nodes);

        // 左边最后一个的next是右边
        leftEnd.right = right;
        
    }
}