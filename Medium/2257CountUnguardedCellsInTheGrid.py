# 0 represents unoccupied and not guarded spots, 1 represents guards and walls
# 2 represents places where guards can see
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in guards + walls:
            grid[i][j] = 1
            
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, j in guards:
            for x, y in dirs:
                cur_i, cur_j = i + x, j + y
                while 0 <= cur_i < m and 0 <= cur_j < n and grid[cur_i][cur_j] != 1:
                    grid[cur_i][cur_j] = 2
                    cur_i += x
                    cur_j += y

        return sum(not grid[i][j] for i in range(m) for j in range(n))
