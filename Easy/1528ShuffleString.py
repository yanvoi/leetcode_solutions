class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        placement = dict()
        for char_index, new_index in enumerate(indices):
            placement[new_index] = s[char_index]
            
        return ''.join(placement[i] for i in range(len(s)))
        
