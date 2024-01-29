# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        if root is None:
            return ''
        
        serialized_list = []

        def serailize_helper(root, serialized_list):
            serialized_list.append(str(root.val))
            for child in root.children:
                serailize_helper(child, serialized_list)
            serialized_list.append('#')

        serailize_helper(root, serialized_list)
        return ','.join(serialized_list)
		    
    def deserialize(self, data):

        if not data or data == "":
            return None

        index = [0]
        data_list = data.split(',')

        def deserialize_helper(data_list, index):
            
            if index[0] == len(data_list):
                return None

            cur = Node(data_list[index[0]], [])
            index[0] = index[0] + 1
            while data_list[index[0]] != '#':
                cur.children.append(deserialize_helper(data_list, index))

            index[0] = index[0] + 1
            return cur

        return deserialize_helper(data_list, index)
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
