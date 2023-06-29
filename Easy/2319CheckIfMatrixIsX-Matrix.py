class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    if not (i == j or i == n - j - 1):
                        return False
                elif i == j or i == n - j - 1:
                    return False

        return True
