class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.triangle = triangle
        return self.dfs(0, 0)


    @cache
    def dfs(self, i, j):

        if i == len(self.triangle):
            return 0

        return self.triangle[i][j] + min(self.dfs(i+1, j), self.dfs(i+1, j+1))
