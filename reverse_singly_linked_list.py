# https://leetcode.com/problems/reverse-linked-list/description/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            # first cache the next node
            next_temp = curr.next
            # change the pointer
            curr.next = prev
            # now move
            prev = curr
            curr = next_temp
            
        return prev