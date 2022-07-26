class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        chars = set()
        
        for letter in sentence:
            chars.add(letter)
            
        if len(chars) == 26:
                return True
        return False
