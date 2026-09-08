# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        traverse = head
        while traverse is not None:
            if traverse in seen:
                return True
            else:
                seen.add(traverse)
                traverse = traverse.next
        return False