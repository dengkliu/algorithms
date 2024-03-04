# https://leetcode.com/problems/delete-nodes-and-return-forest/description/

# Delete Nodes And Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """

        if root is None:
            return []

        result = []

        def dfs(root, to_delete, parent_deleted):
            if root is None:
                return None
            
            # First check if it is a new root
            if parent_deleted and root.val not in to_delete:
                result.append(root)

            current_deleted = root.val in to_delete    
            
            # we still need to process left and right child 
            # regardless of whether the current node needs to be deleted or not
            root.left = dfs(root.left, to_delete, current_deleted)
            root.right = dfs(root.right, to_delete, current_deleted)

            # This is how we remove a node, we return None to its parent node
            if current_deleted:
                return None
            
            return root
        
        dfs(root, to_delete, True)

        return result
