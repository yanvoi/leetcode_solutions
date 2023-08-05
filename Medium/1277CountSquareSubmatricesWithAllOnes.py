class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] *= min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1

        return sum(sum(row) for row in matrix)
