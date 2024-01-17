# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result = []

        self.postorder(root, result)

        return result

    def postorder(self, root, result):
        if root.left:
            self.postorder(root.left, result)
        if root.right:
            self.postorder(root.right, result)
        result.append(root.val)
    
    def postorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, result, visited = [], [], []
        stack.append(root)
        # 用一个boolean记录这个node的左右子树是否被访问了
        visited.append(False)

        while stack:
            cur = stack.pop()
            cur_visited = visited.pop()
            if not cur_visited:
                stack.append(cur)
                visited.append(True)
                if cur.right:
                    stack.append(cur.right)
                    visited.append(False)
                if cur.left:
                    stack.append(cur.left)
                    visited.append(False)
            else:
                result.append(cur.val)
        
        return result
