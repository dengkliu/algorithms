public class Solution {

	List<TreeNode> inorderTraveral(TreeNode root) {
		List<TreeNode> inorder = new ArrayList<>();

		if (root == null) {
			return inorder;
		}

		TreeNode dummy = new TreeNode(0);
		dummy.right = root;
		Stack<TreeNode> stack = new Stack<>();

		stack.push(dummy);

		while(!stack.isEmpty()) {

			TreeNode node = stack.pop();

			if (node.right != null) {

				node = node.right;

				// 先一直往左走
				while (node != null) {
					stack.push(node);
					node = node.left;
				}				
			}

			if (!stack.isEmpty()) {
				inorder.add(stack.peek());
			}
		}

		return inorder;
	}

}