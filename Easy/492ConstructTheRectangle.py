class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        L = int(math.sqrt(area))
        
        while area % L != 0:
            L -= 1
            
        return [area // L, L]
        
