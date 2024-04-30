# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# We run a preorder depth-first search (DFS) on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output traversal of this traversal, recover the tree and return its root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        # why do we need a depth to nodes map?
        # and why don't we add root to it?
        depth_to_nodes = collections.defaultdict(list)
        index = 0
        cur_depth = 0

        while index < len(traversal):
            if traversal[index] != '-':
                # why do we have a while loop here to get number?
                num = int(traversal[index])
                index += 1
                while index < len(traversal) and traversal[index] != '-':
                    num = num*10 + int(traversal[index])
                    index += 1
                node =  TreeNode(num)
                depth_to_nodes[cur_depth].append(node)
                parent_level_nodes = depth_to_nodes[cur_depth - 1]
                # why do we check if parent level nodes exist or not?
                if parent_level_nodes:
                    parent = parent_level_nodes[-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                # reset the depth
                cur_depth = 0
            else:
                index += 1
                cur_depth += 1
        
        return depth_to_nodes[0][0]
            