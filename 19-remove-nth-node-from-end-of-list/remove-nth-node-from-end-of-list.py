# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next
        
        n = i - n #the index of node that needs to be deleted
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for j in range(n):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next