class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        ans = set()
        
        # looping over the grid horizontally
        for i in range(len(grid)):
            curr = set()
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr.add((i, j))
            if len(curr) > 1:
                ans = ans.union(curr)
              
        # looping over the grid perpendicularly
        for j in range(len(grid[0])):
            curr = set()
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    curr.add((i, j))
            if len(curr) > 1:
                ans = ans.union(curr)
                
        return len(ans)
        
