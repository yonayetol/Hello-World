# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow = fast = head
        i = 0
        while fast and fast.next:
            i += 1
            fast = fast.next.next
            slow = slow.next
        # slow = the middle node(if two the later one
        print(i," = i")
        prev = None
        curr = slow
        while curr:
            tempo = curr.next
            curr.next = prev
            prev = curr
            curr = tempo
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True