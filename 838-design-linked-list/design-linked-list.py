class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next  
        i = 0
        while curr and i != index:
            curr = curr.next
            i += 1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next  
        self.head.next = new_head 
        if self.tail == self.head:
            self.tail = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        self.tail.next = new_tail 
        self.tail = new_tail 

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return self.addAtHead(val)  
        if index == 0:
            return self.addAtHead(val) 

        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1

        if curr is None:
            return  
        # Insert the new node
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        
        if new_node.next is None:  
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return  # Invalid index

        curr = self.head
        i = 0
        while curr.next and i < index:
            curr = curr.next
            i += 1

        if curr.next is None:  # Index is out of bounds
            return
        
        # If we're deleting the head
        if index == 0:
            self.head.next = curr.next.next
            if self.head.next is None: 
                self.tail = self.head

        else:  
            curr.next = curr.next.next
            if curr.next is None: 
                self.tail = curr  
