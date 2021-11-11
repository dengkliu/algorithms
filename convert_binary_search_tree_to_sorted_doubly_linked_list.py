# https://www.lintcode.com/problem/1534

# Convert a BST to a sorted circular doubly-linked list in-place. 
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, 
# the predecessor of the first element is the last element, and the successor of the last element is the first element

# Input: {4,2,5,1,3}
#        4
#       /  \
#      2    5
#     / \
#    1   3
# Output: "left:1->5->4->3->2  right:1->2->3->4->5"
# Explanation:
# Left: reverse output
# Right: positive sequence output

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):

        if root is None:
            return None

        stack = []
        result = []

        dummy = TreeNode(0)

        dummy.right = root

        stack.append(dummy)

        while stack:
            node = stack.pop()
            if node.right is not None:
                node = node.right
                stack.append(node)
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left   
            if stack:         
                result.append(stack[-1])
            
            length = len(result)
            if length > 1:
                prev = result[length - 2]
                tail = result[length - 1]
                prev.right = tail
                tail.left = prev
        
        firstNode = result[0]
        lastNode = result[-1]

        firstNode.left = lastNode
        lastNode.right = firstNode

        return result[0]
