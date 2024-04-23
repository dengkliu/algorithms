# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:
# Input: root = [0]
# Output: [0]

# The number of nodes in the tree is in the range [1, 104].
# -10^5 <= Node.val <= 10^5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        # max frequency and the corresponding number
        max_fre = 0
        max_fre_num = float('-inf')
        # the frequency of currnet number, we want to compare it with the max frequency
        curr_fre = float('-inf')
        # the previous number, by comparing current number and previous number
        # we can determine the frequency, it's because we do in-order traversal 
        # so the numbers are always sorted
        previous = float('-inf')

        if root is None:
            return result

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        while stack:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                stack.append(curr)
                while curr.left:
                    curr = curr.left
                    stack.append(curr)

            if stack:
                curr = stack[-1]
                if curr.val != previous:
                    curr_fre = 1
                    previous = curr.val
                elif curr.val == previous:
                    curr_fre += 1
                
                if curr_fre == max_fre:
                    result.append(curr.val)
                elif curr_fre > max_fre:
                    max_fre_num = curr.val
                    max_fre = curr_fre
                    result = [curr.val]
        
        return result