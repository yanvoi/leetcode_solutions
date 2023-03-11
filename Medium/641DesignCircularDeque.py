class DequeNode:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None


class MyCircularDeque:

    def __init__(self, k: int):
        # setting up dummy nodes
        self.head, self.tail = DequeNode(None), DequeNode(None)
        self.head.next, self.tail.prev = self.tail, self.head

        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False

        new_node = DequeNode(value)

        new_node.prev = self.head
        new_node.next = self.head.next
        new_node.next.prev = new_node
        self.head.next = new_node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False

        new_node = DequeNode(value)

        new_node.next = self.tail
        new_node.prev = self.tail.prev
        new_node.prev.next = new_node
        self.tail.prev = new_node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False

        to_delete = self.head.next
        self.head.next = to_delete.next
        to_delete.next.prev = self.head

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False

        to_delete = self.tail.prev
        self.tail.prev = to_delete.prev
        to_delete.prev.next = self.tail

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
