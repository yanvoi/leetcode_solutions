# algorithmic solution without returning n - 1
class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n > 1:
            answer += n // 2
            n = n // 2 + n % 2

        return answer
