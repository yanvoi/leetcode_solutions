class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer = []
        strength = [[] for _ in range(len(mat[0]) + 1)]
        for i, row in enumerate(mat): strength[sum(row)].append(i)
        for i in range(len(mat[0]) + 1):
            for index in strength[i]:
                if not k: return answer
                answer.append(index)
                k -= 1

        return answer
