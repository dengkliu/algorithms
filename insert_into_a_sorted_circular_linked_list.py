# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal)

        # 1. when empty
        if not head:
            new_node.next = new_node
            return new_node

        # 2. when a single node
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head
        
        pre = head
        cur = head.next

        while cur != head:
            # 1. val between the maximum and minimum of all nodes
            if pre.val <= insertVal and cur.val >= insertVal:
                pre.next = new_node
                new_node.next = cur
                return head
            
            # 2. we found the tail and val not in the range of (max, min)
            if pre.val > cur.val:
                if insertVal <= cur.val or insertVal >= pre.val:
                    pre.next = new_node
                    new_node.next = cur
                    return head
    
            pre = cur
            cur = cur.next
                    
        # 3. we go back to head
        # 3.1 all nodes are identical
        # 3.2 the value is between head and prev node of head
        pre.next = new_node
        new_node.next = cur
        return head	