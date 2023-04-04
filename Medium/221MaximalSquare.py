# brilliant solution by arkaung:
# https://leetcode.com/problems/maximal-square/solutions/600149/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        longest_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    longest_side = max(longest_side, dp[i + 1][j + 1])

        return longest_side ** 2
