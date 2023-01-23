class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trusted_by[a] -= 1
            trusted_by[b] += 1

        for person in range(1, n + 1):
            if trusted_by[person] == n - 1:
                return person

        return -1
