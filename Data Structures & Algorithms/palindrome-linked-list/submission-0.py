# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        #brute force, 2 loops, turn into a list then run 2 ptr
        curr = head
        check = []
        while curr is not None:
            check.append(curr.val)
            curr = curr.next
        l, r = 0, len(check)-1
        while l < r:
            if check[l] != check[r]:
                return False
            l, r = l+1, r-1
        return True