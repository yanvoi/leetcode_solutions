class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        m, n = len(land), len(land[0])
        def dfs(i, j):
            if not(0 <= i < m) or not(0 <= j < n) or not land[i][j]:
                return (-1, -1)

            land[i][j] = 0

            down_row, down_col = dfs(i + 1, j)
            right_row, right_col = dfs(i, j + 1)

            row = max(i, down_row, right_row)
            col = max(j, down_col, right_col)

            return (row, col)

        answer = []
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    x, y = dfs(i, j)
                    answer.append([i, j, x, y])

        return answer
