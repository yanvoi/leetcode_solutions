# simply simulate the process by 'rotting' oranges adjacent to rotten oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        rotten = collections.deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        minutes_passed = 0
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while rotten and fresh:
            minutes_passed += 1
            size = len(rotten)
            for _ in range(size):

                i, j = rotten.popleft()
                for x, y in adj:
                    row, column = i + x, j + y

                    if not (0 <= row < m) or not (0 <= column < n):
                        continue
                    if grid[row][column] == 0 or grid[row][column] == 2:
                        continue

                    grid[row][column] = 2
                    fresh -= 1
                    rotten.append((row, column))

        return -1 if fresh else minutes_passed
