public class Solution {

	public List<Integer> preOrderTraversal(TreeNode root) {

		Stack<TreeNode> stack = new Stack<>();
		List<Integer> preroder = new ArrayList<>();

		if (root == null) {
			return preorder;
		}

		stack.push(root);

		while(!stack.empty()) {

			TreeNode = stack.pop();

			preorder.add(node.val);

			if (node.right != null) {
				stack.push(node.right);
			}

			if (node.left != null) {
				stack.push(node.left);
			}
		}

		return preorder;
	}
}