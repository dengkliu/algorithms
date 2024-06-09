# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if queue and i != size - 1:
                    curr.next = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return root

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # we can do this because it is a perfect binary tree!
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
