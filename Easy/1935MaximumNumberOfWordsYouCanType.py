class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        broken = set(brokenLetters)
        
        words = text.split()
        count = len(words)
        
        for word in words:
            for char in word:
                if char in broken:
                    count -= 1
                    break
                    
        return count
        
