class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:

        is_zero = {(x, y) for x, y in mines}
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            left = right = up = down = 0
            for j, k in zip(range(n), range(n-1, -1, -1)):
                up = 0 if (i, j) in is_zero else up + 1
                down = 0 if (i, k) in is_zero else down + 1
                left = 0 if (j, i) in is_zero else left + 1
                right = 0 if (k, i) in is_zero else right + 1

                dp[i][j] = min(dp[i][j], up)
                dp[i][k] = min(dp[i][k], down)
                dp[j][i] = min(dp[j][i], left)
                dp[k][i] = min(dp[k][i], right)

        return max(max(row) for row in dp)
