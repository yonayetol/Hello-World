# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head2 = head
        while head2:
            last = head
            cur = head.next
            while cur:
                if last.val >= x and cur.val < x:
                    forward,prev = cur.val,last.val
                    last.val = forward
                    cur.val = prev
                    
                cur = cur.next
                last = last.next
                
            head2 = head2.next
        return head
