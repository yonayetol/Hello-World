# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is now on the starting point of the next half and prev is before it
        prev.next = None # breaking the relation between first and second half
        dummy, fast = ListNode(), slow
        slow = dummy
        while fast:
            tempo = fast.next
            fast.next = slow
            slow = fast
            if not tempo:
                break 
            fast = tempo
        # dummy is the reversed linked list now
        the_max = 0
        while slow.val != 0: # till the dummy node malet new
            the_max = max((head.val + slow.val), the_max)
            head, slow = head.next, slow.next
        return the_max

