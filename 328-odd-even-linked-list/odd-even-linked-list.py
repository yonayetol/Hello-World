# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        if length < 3:
            return head

        odd = head
        even = head.next
        for i in range(length//2):
            odd.next = even.next
            
            even.next = None
            tail.next = even
            tail = tail.next

            odd = odd.next
            even = odd.next

        return head