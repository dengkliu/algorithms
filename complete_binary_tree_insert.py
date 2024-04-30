# https://leetcode.com/problems/complete-binary-tree-inserter/

# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

# Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

# Implement the CBTInserter class:

# CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.level_to_nodes = {}
        self.last_level = 0
        self.level_to_insert = 0
        self.index_to_insert = 0

        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            nodes = []
            for i in range(size):
                node = queue.popleft()
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            self.level_to_nodes[self.last_level] = nodes
            # why do we check if queue is none or not?
            if queue:
                self.last_level += 1

        # if the last level is not complete, then we should insert node to it, 
        # by adding nodes as child to previous level
        if len(self.level_to_nodes[self.last_level]) < pow(2, self.last_level):
            self.level_to_insert = self.last_level - 1
            self.index_to_insert = len(self.level_to_nodes[self.last_level])/2
        else:
            self.level_to_insert = self.last_level
            self.index_to_insert = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node_to_insert = TreeNode(val)
        level_to_insert_node = self.level_to_nodes[self.level_to_insert]
        node_parent = level_to_insert_node[self.index_to_insert]

        if not node_parent.left:
            node_parent.left = node_to_insert
        else:
            node_parent.right = node_to_insert
            self.index_to_insert += 1
        
        # this means the node just got inserted into a new level
        if self.last_level == self.level_to_insert:
            self.last_level += 1
            self.level_to_nodes[self.last_level] = [node_to_insert]
        # the node got inserted into an existing level
        # now we want to check if it's complete or not
        # if complete, then we should starting inserting into a new level
        else:
            self.level_to_nodes[self.last_level].append(node_to_insert)
            if len(self.level_to_nodes[self.last_level]) == pow(2, self.last_level):
                self.level_to_insert = self.last_level
                self.index_to_insert = 0
           
        return node_parent.val
    
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.level_to_nodes[0][0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()