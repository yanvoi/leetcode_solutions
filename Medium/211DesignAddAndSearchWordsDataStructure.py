class TrieNode:
    
    def __init__(self, char=''):
        
        self.children = dict()
        self.is_word = False

        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word: str):
        
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            
        node.is_word = True
        
    def search(self, word: str, index: int, node=None):
        
        if node is None: node = self.root
        
        for i in range(index, len(word)):
            if word[i] == '.':
                for child in node.children.values():
                    if self.search(word, i+1, child):
                        return True
                    
                return False
            
            if word[i] not in node.children:
                return False
                
            node = node.children[word[i]]
        
        return node.is_word


class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        self.longest = 0

    def addWord(self, word: str) -> None:
        self.trie.add(word)
        self.longest = max(self.longest, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.longest: return False
        return self.trie.search(word, 0)

    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
