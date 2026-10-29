# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass find 
        p = ListNode(0, head)
        s,f = p,head
        for _ in range(n):
            f = f.next
        while f is not None:
            s, f = s.next, f.next
        s.next = s.next.next
        return s.next if s == p else head
        