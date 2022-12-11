class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        max_vertically = [0 for _ in range(len(grid))]
        max_horizontally = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_vertically[i] = max(max_vertically[i], grid[i][j])
                max_horizontally[j] = max(max_horizontally[j], grid[i][j])

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                possible_gain = min(max_vertically[i], max_horizontally[j]) - grid[i][j]
                answer += possible_gain if possible_gain > 0 else 0

        return answer
