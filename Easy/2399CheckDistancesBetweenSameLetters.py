class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indexes = dict()
        
        for i, char in enumerate(s):
            if char in indexes:
                if i - indexes[char] - 1 != distance[ord(char) - 97]:
                    return False
            else:
                indexes[char] = i
            
        return True
    
