# O(n) time, O(1) space
class Solution:
    def maxPower(self, s: str) -> int:
        answer, cur = 1, 1
        for i in range(1, len(s)):
            cur = cur + 1 if s[i] == s[i - 1] else 1
            answer = max(answer, cur)

        return answer
