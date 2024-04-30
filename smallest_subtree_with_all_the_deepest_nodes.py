# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        deepest_nodes = [root.val]
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            curr_level = []
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    curr_level.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    curr_level.append(curr.right.val)
            # Why do we want to check queue size here?
            if queue:
                deepest_nodes = curr_level

        def lowest_common_ancestor(root, deepest_nodes):

            if not root:
                return None

            if root.val in deepest_nodes:
                return root
            
            l = lowest_common_ancestor(root.left, deepest_nodes)
            r = lowest_common_ancestor(root.right, deepest_nodes)

            if l and r:
                return root
            else:
                return l or r
        
        return lowest_common_ancestor(root, deepest_nodes)
