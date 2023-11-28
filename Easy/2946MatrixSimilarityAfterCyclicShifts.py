class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(mat[i][j] == mat[i][(j + k) % len(mat[0])] for i in range(len(mat)) for j in range(len(mat[0])))
