// https://www.lintcode.com/problem/1534

// Convert a BST to a sorted circular doubly-linked list in-place. 
// Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

// We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, 
// the predecessor of the first element is the last element, and the successor of the last element is the first element

// Input: {4,2,5,1,3}
//        4
//       /  \
//      2   5
//     / \
//    1   3
// Output: "left:1->5->4->3->2  right:1->2->3->4->5"
// Explanation:
// Left: reverse output
// Right: positive sequence output

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
     * @param root: root of a tree
     * @return: head node of a doubly linked list
     */
    public TreeNode treeToDoublyList(TreeNode root) {

        if (root == null) {
            return null;
        }

        List<TreeNode> nodes = new ArrayList<>();

        inOrderHelper(root, nodes);

        TreeNode minNode = nodes.get(0);
        TreeNode maxNode = nodes.get(nodes.size() - 1);

        minNode.left = maxNode;
        maxNode.right = minNode;

        return minNode;
    }

    void inOrderHelper(TreeNode node, List<TreeNode> nodes) {

        if (node == null) {
            return;
        }

        inOrderHelper(node.left, nodes);
        nodes.add(node);
        if (nodes.size() >= 2) {
            TreeNode preNode = nodes.get(nodes.size() - 2);
            preNode.right = node;
            node.left = preNode;
        }
        inOrderHelper(node.right, nodes);
    }
}