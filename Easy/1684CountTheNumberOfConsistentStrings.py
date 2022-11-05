class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ans = len(words)
        available = set(allowed)
        
        for word in words:
            for char in word:
                if char not in available:
                    ans -= 1
                    break
            
        return ans
        
