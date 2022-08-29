class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        unique = set()
        for num in freq.values():
            if num in unique:
                return False
            unique.add(num)
            
        return True
        
