class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
                
        if count == len(word) or (count == 1 and word[0].isupper()) or count == 0:
            return True
        
        return False
        
