# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        head = ListNode(0)
        curr = head
        while l1 != None  or l2 != None or overflow !=0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            val = l1Val + l2Val + overflow
            overflow = val // 10
            newNode = ListNode(val  % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        return head.next
                
                
            