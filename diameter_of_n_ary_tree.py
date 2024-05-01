# https://leetcode.com/problems/diameter-of-n-ary-tree/

# Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """

        if not root:
            return 0

        longest_path = [0]

        result = [0]

        def dfs(root):

            if not root.children:
                return 0

            if len(root.children) == 1:
                child_path = dfs(root.children[0])
                result[0] = max(result[0], 1 + child_path)
                return 1 + child_path

            top_1_path = 0
            top_2_path = 0
            
            for child in root.children:
                child_path = dfs(child)
                if child_path > top_1_path:
                    top_1_path, top_2_path = child_path, top_1_path
                elif child_path > top_2_path:
                    top_2_path = child_path
            
            result[0] = max(result[0], top_1_path + 1 + top_2_path + 1)

            return top_1_path + 1
        
        dfs(root)

        return result[0]