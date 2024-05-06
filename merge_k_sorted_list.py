# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        # start merging from neighboring list
        interval = 1
        while interval < len(lists):
            for index in range(0, len(lists) - interval, interval * 2):
                list1 = lists[index]
                list2 = lists[index + interval]
                lists[index] = self._merge_two_lists(list1, list2)
            
            interval = interval * 2
        
        return lists[0]


    def _merge_two_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        # why do we need a dummy
        dummy = head

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        return head.next