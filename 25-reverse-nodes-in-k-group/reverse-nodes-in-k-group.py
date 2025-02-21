# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Function to reverse a portion of the linked list
        def reverseLinkedList(start: ListNode, k: int) -> ListNode:
            prev = None
            curr = start
            while k > 0:
                next_node = curr.next  # Store next node
                curr.next = prev  # Reverse the link
                prev = curr  # Move prev to current
                curr = next_node  # Move to the next node
                k -= 1
            return prev  # New head of the reversed portion

        # Check if there are at least k nodes left in the list
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count == k:  # Only reverse if there are k nodes
            # Reverse k nodes
            new_head = reverseLinkedList(head, k)
            # head is now the end of the reversed portion, connect it to the next part
            head.next = self.reverseKGroup(curr, k)  # Recurse for the next portion
            return new_head  # Return new head after reversal
        else:
            return head  # If less than k nodes remain, return head as is