# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val < list2.val:
                result.append(ListNode(list1.val))
                list1 = list1.next
            else:
                result.append(ListNode(list2.val))
                list2 = list2.next

        while list1:
            result.append(ListNode(list1.val))
            list1 = list1.next

        while list2:
            result.append(ListNode(list2.val))
            list2 = list2.next

        for l1, l2 in zip(result, result[1:]):
            l1.next = l2
        
        return result[0]