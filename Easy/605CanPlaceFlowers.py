class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                n -= 1
                if n <= 0: return True
                i += 2
            else:
                i += 1
                
        return n <= 0
        
