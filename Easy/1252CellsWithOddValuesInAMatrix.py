# time O(m * n), space O(max(m, n))
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        answer = 0
        for row in rows:
            for col in cols:
                answer += (row + col) % 2 == 1

        return answer

# time O(m * n), space O(n^2)
# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         rows, cols = [0] * m, [0] * n
#         for r, c in indices:
#             rows[r] += 1
#             cols[c] += 1
        
#         return sum((row + col) % 2 == 1 for row in rows for col in cols)
