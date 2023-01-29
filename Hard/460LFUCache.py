class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DoubleLinkedList:

    def __init__(self):
        self._dummy = Node(None, None) # dummy node
        self._dummy.next = self._dummy.prev = self._dummy
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._dummy.next
        node.prev = self._dummy
        node.next.prev = node
        self._dummy.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self._dummy.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node
        

class LFUCache:
    def __init__(self, capacity):

        self._size = 0
        self._capacity = capacity
        
        self._node = dict()
        # each frequency has it's own double linked list
        self._freq = defaultdict(DoubleLinkedList)
        self._minfreq = 0
        
        
    def _update(self, node):

        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):

        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):

        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
            return

        if self._size == self._capacity:
            node = self._freq[self._minfreq].pop()
            del self._node[node.key]
            self._size -= 1
            
        node = Node(key, value)
        self._node[key] = node
        self._freq[1].append(node)
        self._minfreq = 1
        self._size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
