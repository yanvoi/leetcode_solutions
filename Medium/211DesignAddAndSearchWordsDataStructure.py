class TrieNode:
    
    def __init__(self, char=''):
        
        self.char = char
        self.children = dict()
        self.is_word = False

        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word: str):
        
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            
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
        
        if node.is_word: return True
        return False


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
