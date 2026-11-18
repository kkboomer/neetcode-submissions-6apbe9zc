# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        l, r = head, head
        for i in range(right - left):
            r = r.next
        prev1 = None
        for i in range(1, left):
            l, r, prev1 = l.next, r.next, l
        # LL reversal
        cont = r.next
        prev, curr = cont, l
        while curr != cont:
            later = curr.next
            curr.next = prev
            prev = curr
            curr = later
        # reattachment
        if left == 1:
            head = prev
        else:
            prev1.next = prev
        return head