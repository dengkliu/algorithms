# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list_len = 0
        front = None
        end = None
        cur = head

        while cur:
            list_len += 1
            if end:
                end = end.next
            if list_len == k:
                front = cur
                end = head  
            cur = cur.next
        
        temp = front.val
        front.val = end.val
        end.val = temp

        return head