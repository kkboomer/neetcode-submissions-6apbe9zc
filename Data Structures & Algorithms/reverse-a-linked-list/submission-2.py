# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        if head.next.next == None:
            newHead = head.next
            head.next, newHead.next = None, head
            return newHead
        t,c,n = None, head, head.next
        while n != None:
            c.next = t
            t, c, n = c, n, n.next
        c.next = t
        return c