class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            
        node.is_end_of_word = True
        
    def find_in_dict(self, word):
        
        path = []
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            
            path.append(char)
            node = node.children[char]
            if node.is_end_of_word:
                return ''.join(path)
            
        return None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)
            
        ans = []
        sentence_copy = sentence.split()
        for word in sentence_copy:
            ret = trie.find_in_dict(word)
            
            if ret:
                ans.append(ret)
            else:
                ans.append(word)
                
        return ' '.join(ans)
        
