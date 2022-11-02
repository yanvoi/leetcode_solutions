class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = [[False] * 3 for _ in range(10)]
        col = {'R' : 0, 'G' : 1, 'B': 2}
        ans = 0
        
        for i in range(0, len(rings) - 1, 2):
            rods[int(rings[i+1])][col[rings[i]]] = True
            
        for rod in rods:
            if rod[0] and rod[1] and rod[2]:
                ans += 1
                
        return ans
        
