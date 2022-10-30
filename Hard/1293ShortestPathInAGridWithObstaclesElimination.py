class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # BFS algorithm using sets to remember which places we've already visited
        # way better than DFS because we end the process when the shortest route is found
        
        # edge case
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        
        # the queue holds i, j indices, num of obstacles eliminated so far, num of steps so far
        q = collections.deque([(0, 0, 0, 0)])
        # i, j indices, num of obstacles we eliminated so far
        # since we can get to every point in a number of ways
        # the set allows us to not check the same route many times
        visited = set()
        m, n = len(grid), len(grid[0])
        
        while q:
            row, col, obstacles, steps = q.popleft()
            
            for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if not 0 <= i < m or not 0 <= j < n:
                    continue
                    
                if i == m - 1 and j == n - 1:
                    return steps + 1
                    
                if grid[i][j] == 1 and obstacles < k and (i, j, obstacles+1) not in visited:
                    visited.add((i, j, obstacles + 1))
                    q.append((i, j, obstacles+1, steps+1))

                if grid[i][j] == 0 and (i, j, obstacles) not in visited:
                    visited.add((i, j, obstacles))
                    q.append((i, j, obstacles, steps+1))
                    
        return -1
        
