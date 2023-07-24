class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        answer = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                answer[i][j] = max(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))

        return answer
