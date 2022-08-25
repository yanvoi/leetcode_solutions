class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        available = dict()
        for char in magazine:
            available[char] = available.get(char, 0) + 1
            
        needed = dict()
        for char in ransomNote:
            needed[char] = needed.get(char, 0) + 1
        
        for char in needed:
            if char not in available or needed[char] > available[char]: return False
        
        return True
        
