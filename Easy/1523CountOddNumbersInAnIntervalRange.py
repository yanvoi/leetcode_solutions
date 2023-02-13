class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        # odd in (0, high + 1) - odd in (0, low)
        return (high + 1) // 2 - low // 2
