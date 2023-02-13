class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)
        queue = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        # if there's only land on the grid
        if len(queue) == n * n:
            return -1
        # we use the manhattan distance meaning we only visit adjacent cells during each iteration
        adjacent = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        distance = 0

        # standard BFS
        while queue:
            size = len(queue)
            for _ in range(size):

                i, j = queue.popleft()
                for x, y in adjacent:
                    if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y] == 0:
                        queue.append((i + x, j + y))
                        grid[i + x][j + y] = 1

            distance += 1

        # (- 1) because during the last while loop we increased the distance
        # even though we did not find any cells satisfying the outcome
        return distance - 1
