# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # take the min from either list
        # increment respective ptr
        # once one of the lists is empty, go through the other one and just add on.
        # return newhead
        dummy = ListNode(0)
        l1, l2 =list1, list2
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1= l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next 
                curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

