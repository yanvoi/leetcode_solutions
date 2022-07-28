class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def get_bits(num):
            count = 0
            while num:
                count += num & 1
                num = num >> 1
            return count
        
        return sorted(arr, key=lambda x: (get_bits(x), x))
    
