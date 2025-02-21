# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        sets,cur = set(), head
        sets.add(head.val)
        
        while cur:
            prev = cur
            while cur and cur.val in sets:
                cur = cur.next

            if cur and cur.val not in sets:
                prev.next = cur
                sets.add(cur.val)
            else:
                prev.next = None
        return head
