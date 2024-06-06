# https://leetcode.com/problems/closest-binary-search-tree-value/

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        stack = []
        dummy = TreeNode(0)
        dummy.right = root
        stack.append(dummy)
        diff = float('inf')
        result = -1
        while stack:
            curr = stack.pop()
            if curr.right:
                next_node = curr.right
                stack.append(next_node)
                while next_node.left:
                    stack.append(next_node.left)
                    next_node = next_node.left
            
            # why do we need to check both?
            if stack and abs(stack[-1].val - target) < diff:
                diff = abs(stack[-1].val - target)
                result = stack[-1].val
            else:
                break
            
        return result


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff = [float('inf')]
        result = [-1]

        def inorder(root):
            if root.left:
                inorder(root.left)

            if abs(root.val - target) < diff[0]:
                diff[0] = abs(root.val - target)
                result[0] = root.val
            else:
                return

            if root.right:
                inorder(root.right)


        inorder(root)

        return result[0]
        
        