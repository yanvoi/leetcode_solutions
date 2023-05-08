class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        total_sum = sum(mat[i][i] + mat[i][len(mat)-i-1] for i in range(len(mat)))
        return total_sum if len(mat) % 2 == 0 else total_sum - mat[len(mat) // 2][len(mat) // 2]
