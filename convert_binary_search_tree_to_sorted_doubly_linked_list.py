# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

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
        
        # stack 用来做inorder traversal模板
        while stack:
            node = stack.pop()
            # 每个节点出来 这个节点和它的左子树都已经被加到result里面去了
            # 所以只看其右子树
            if node.right is not None:
                node = node.right
                # 对于每个节点，都是先入栈，然后把左子树入栈 左子树的左子树 ..。
                stack.append(node)
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left
            
            # 把最后一个入栈的节点加入到result
            if stack:         
                result.append(stack[-1])
            
            # 把结果里的后两个节点串起来
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
