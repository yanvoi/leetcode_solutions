class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        answer = 0
        for i in range(n):
            answer ^= start + 2 * i

        return answer
