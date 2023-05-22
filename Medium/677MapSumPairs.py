class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.get_sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# my own raw implementation of a prefix tree after a long time
class TrieNode:

    def __init__(self):
        self.children = dict()
        self.val = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, val):
        root = self.root
        for letter in key:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]

        root.val = val

    def get_sum(self, prefix):
        def sum_from_here(root):
            total_sum = 0
            stack = [root]
            while stack:
                node = stack.pop()
                total_sum += node.val
                for child in node.children.values():
                    stack.append(child)
            return total_sum
            
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                return 0
            root = root.children[letter]

        return sum_from_here(root)
