# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode((l1.val + l2.val)%10)
        curr, l1, l2, carry = dummy, l1.next, l2.next, (l1.val + l2.val)//10

        while l1 or l2:
            first = sec = 0
            if l1: first, l1 = l1.val, l1.next
            if l2: sec,l2 = l2.val, l2.next

            curr.next,carry = ListNode((first + sec + carry)%10), (first + sec + carry) // 10
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)
        return dummy
