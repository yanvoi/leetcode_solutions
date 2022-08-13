class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = dict()
        
        for word in strs:
            key = tuple(sorted(word))
            h[key] = h.get(key, []) + [word]
            
        return list(h.values())
        
