# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack = []
        dummy = TreeNode()
        dummy.right = root
        stack.append(dummy)
        range_sum = 0
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                stack.append(node)
                while node.left:
                    stack.append(node.left)
                    node = node.left
            if stack:
                if stack[-1].val >= low and stack[-1].val <= high:
                    range_sum += stack[-1].val
                if stack[-1].val > high:
                    break
        return range_sum