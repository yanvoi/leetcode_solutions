class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        h = dict()
        
        for i in range(len(pattern)):
            if pattern[i] in h:
                if h[pattern[i]] != words[i]:
                    return False
            else:
                h[pattern[i]] = words[i]
                
        if len(set(h.values())) != len(h.values()):
            return False
        
        return True
        
