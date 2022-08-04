class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if not self.head:
            return -1
        
        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val)
            
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            node = self.head
            
            for i in range(index - 1):
                node = node.next
            
            new_node.next = node.next
            node.next = new_node
        
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        node = self.head
        if index == 0:
            self.head = node.next
        else:
            for i in range(index - 1):
                node = node.next
            node.next = node.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
