class CustomListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()

        self.head = CustomListNode(0, 0)
        self.tail = CustomListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:

        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._delete_node(node)
            self._add_node(node)
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.key_to_node:
            self._delete_node(self.key_to_node[key])

        new_node = CustomListNode(key, value)
        self._add_node(new_node)
        self.key_to_node[key] = new_node

        if len(self.key_to_node) > self.capacity:
            node_to_delete = self.tail.prev
            self._delete_node(node_to_delete)
            del self.key_to_node[node_to_delete.key]

        
    def _add_node(self, node):
        buffer_node = self.head.next
        node.next = buffer_node
        buffer_node.prev = node
        node.prev = self.head
        self.head.next = node


    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
