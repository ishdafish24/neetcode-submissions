# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        prev = None
        curr = head
        if head.next is None:
            return curr
        nxt = head.next
        while nxt is not None:
            curr.next = prev
            n_copy = nxt.next
            nxt.next = curr
            prev = curr
            curr = nxt
            nxt = n_copy
        return curr


        