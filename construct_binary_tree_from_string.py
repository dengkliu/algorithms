# https://leetcode.com/problems/construct-binary-tree-from-string/
 
# You need to construct a binary tree from a string consisting of parenthesis and integers.

# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

# You always start to construct the left child node of the parent first if it exists.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
    
        def dfs(s, index):
            if index[0] == len(s):
                return None
            
            def getVal(s):
            	# 1. Why do we need is_negative here
                is_negative = False
                if s[index[0]] == ')':
                    return float('-inf')
                if s[index[0]] == '-':
                    is_negative = True
                    index[0] += 1
                value = 0
                while index[0] < len(s) and s[index[0]] != '(' and s[index[0]] != ')':
                    value = value * 10 + int(s[index[0]])
                    index[0] += 1       
                return value if not is_negative else -value

            value = getVal(s)
            node = None
            if value == float('-inf'):
                return None
            else:
                node = TreeNode(value)

            # If there is left child for this node
            if index[0] < len(s) and s[index[0]] == '(':
                index[0] += 1
                # Left subtree
                node.left = dfs(s, index)
            
            # If there is a right tree for this node
            if node.left and index[0] < len(s) and s[index[0]] == '(':
                index[0] +=1
                node.right = dfs(s, index)
            
            # If this node is a leaf node
            if index[0] < len(s) and s[index[0]] == ")":
                index[0] += 1
                return node
            
            return node
        
        return dfs(s, [0])
