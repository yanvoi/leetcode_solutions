class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        R, C = len(img), len(img[0])
        ans = [[0] * C for _ in range(R)]
        
        for row in range(R):
            for col in range(C):
                
                neighbors = [
                    img[r][c]
                    for r in (row - 1, row, row + 1)
                    for c in (col - 1, col, col + 1)
                    if 0 <= r < R and 0 <= c < C
                ]
                
                ans[row][col] = sum(neighbors) // len(neighbors)
        
        return ans
        
