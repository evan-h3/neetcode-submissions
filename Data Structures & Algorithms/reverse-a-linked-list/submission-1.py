# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, head
        while r:
            next = r.next
            r.next = l
            l = r
            r = next

        return l
    
        