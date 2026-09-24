# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = None
        r = head

        while head and head.next:
            if l == r:
                return True
            l = head
            r = r.next.next
            head = head.next

        return False