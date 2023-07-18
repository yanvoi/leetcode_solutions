# it was extremely unintuitive for me - I had to look up the solution
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        answer = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                answer[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= answer[i][j]
                colSum[j] -= answer[i][j]

        return answer
