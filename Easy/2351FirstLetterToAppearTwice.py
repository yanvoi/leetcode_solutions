class Solution:
    def repeatedCharacter(self, s: str) -> str:
        se = set()
        
        for letter in s:
            if letter in se:
                return letter
            se.add(letter)
        
