# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        head2 = prev

        flag = 1
        dummy = ListNode()
        newList = dummy
        while head and head2:
            if flag:
                dummy.next = head
                head = head.next
                flag = 0
            else:
                dummy.next = head2
                head2 = head2.next
                flag = 1
            dummy = dummy.next
        if head:
            dummy.next = head
        if head2:
            dummy.next = head2
        head = newList

