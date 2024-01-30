# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'

        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        nodes_val = data.split(',')
        # container for the index
        index = [0]

        def deserialize_helper(nodes_val, index):    
            if nodes_val[index[0]] == '#':
                return None
            else:
                cur = TreeNode(int(nodes_val[index[0]]))
                index[0] = index[0] + 1
                cur.left = deserialize_helper(nodes_val, index)
                index[0] = index[0] + 1
                cur.right = deserialize_helper(nodes_val, index)
                return cur
                
        return deserialize_helper(nodes_val, index)
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
