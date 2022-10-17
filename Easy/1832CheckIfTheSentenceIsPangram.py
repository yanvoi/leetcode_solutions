class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letters = set()
        
        for char in sentence:
            letters.add(char)
            if len(letters) == 26: return True
            
        return False
        
