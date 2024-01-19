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

        def delNodes(root, to_delete, parent_deleted):
            if root is None:
                return None
            
            if parent_deleted and root.val not in to_delete:
                result.append(root)
            
            parent_deleted = root.val in to_delete
            
            root.left = delNodes(root.left, to_delete, parent_deleted)
            root.right = delNodes(root.right, to_delete, parent_deleted)

            return None if parent_deleted else root
        
        delNodes(root, to_delete, True)

        return result