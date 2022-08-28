class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = dict()
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
            
        ans = []
        for num in arr2:
            ans = ans + [num] * freq[num]
            del freq[num]
            
        to_append = []
        for num in freq:
            to_append = to_append + [num] * freq[num]
        
        return ans + sorted(to_append)
        
